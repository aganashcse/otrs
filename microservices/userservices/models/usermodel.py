from db import db

class User(db.Model):
    __tablename__ = 'users'
    u_email = db.Column(db.String(50), primary_key=True)
    u_passwd = db.Column(db.String(30))

    def __init__(self, u_email, u_passwd):
        self.u_email = u_email
        self.u_passwd = u_passwd

    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def json(self):
        return {"u_email":self.u_email, "u_passwd":self.u_passwd}
    
    @classmethod
    def find_by_email(cls, u_email):
        return cls.query.filter_by(u_email=u_email).first()