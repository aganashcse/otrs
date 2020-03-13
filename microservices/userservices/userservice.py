from flask import Flask
from flask_restful import Api

from resources.user import UserRegister, GetUser

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1117@0.0.0.0/orts1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'ganesha'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(UserRegister, '/register')
api.add_resource(GetUser, '/get/<string:u_email>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=2222, debug=True)