from flask import Flask, request, url_for, render_template, session, redirect
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

import flask_login
import requests

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
mail = Mail(app)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
s = URLSafeTimedSerializer('Thisisasecret!')
userRegisterUri='http://localhost:2222/register'
userGetUri='http://localhost:2222/get'


#flask_login section
class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):
    user = User()
    user.id = session['email']
    return user

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        if request.form['revw']:
            msg = Message("Review from User:%s!"%(flask_login.current_user.id), sender = app.config["MAIL_USERNAME"], recipients = [app.config["MAIL_USERNAME"]])  
            msg.body = request.form['revw']
            mail.send(msg)
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    session['email']=request.form['email']
    get_user_response = requests.get(userGetUri+'/'+session['email'])
    if get_user_response.status_code == 200:
        print("type:",type(get_user_response.json()))
        print("data:",get_user_response.json())
        if request.form['passwd'] != get_user_response.json().get('u_passwd'):
            return render_template('login.html', msg = 'Password is incorrect!')
        user = User()
        user.id = session['email']
        flask_login.login_user(user)
        return redirect(url_for('index'))
    else:
        return render_template('login.html', msg = 'Email doesn\'t exists! Please register if new user!')

@app.route('/logout', methods=['GET', 'POST'])
@flask_login.login_required
def logout():
    flask_login.logout_user()
    session.clear()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method=='GET':
        return render_template('register.html')
    else:
        session['email'] = request.form['email']
        session['user_info'] = {'u_email': str(session['email']), 'u_passwd': str(request.form['passwd'])}
        re_passwd=request.form['re_passwd']
        if session['user_info']['u_passwd']==re_passwd:
            get_user_response = requests.get(userGetUri+'/'+session['email'])
            #handling if user(s) already exists
            if get_user_response.status_code == 200:
                return render_template('register.html', msg = 'Email already used!!!')
            if get_user_response.status_code == 400:
                token = s.dumps(session['email'], salt='email-confirm')
                msg = Message('OTRS Account Verification Email', sender=app.config["MAIL_USERNAME"], recipients=[session['email']])
                link = url_for('confirm_email', token=token, _external=True)
                msg.body = 'Your link is {}'.format(link)
                mail.send(msg)
                return render_template('login.html', msg = 'Verification link sent to your email. Please verify email and login again. Verification link is valid only for 5 minutes!')
            return render_template('register.html', msg = 'Something is not right!')
        else:
            return render_template('register.html', msg = 'Password Doesn\'t matching! Please re-register')

@app.route('/confirm_email/<token>',methods=['GET'])
def confirm_email(token):
    try:
        email = s.loads(token, salt='email-confirm', max_age=300)
    except SignatureExpired:
        return render_template('register.html', msg = 'The token is expired! Please register again!')
    print("session_data:",session)
    user_post_response = requests.post(url=userRegisterUri, data=session['user_info'])
    if user_post_response.status_code == 201:
        return render_template('login.html', msg = 'Verification successful!. Please login with registered creds.')
    return render_template('login.html', msg = 'something is not right!')

if __name__=='__main__':
    app.secret_key="afdoijaw23409aoj()_)(&%#$%)"
    app.run(debug=True, use_reloader=False, port=1111)
