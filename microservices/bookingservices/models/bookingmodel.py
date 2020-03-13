from db import db

class Booking(db.Model):
    __tablename__ = 'bookings'
    b_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    t_id = db.Column(db.Integer, db.ForeignKey('tables.t_id'))
    u_email = db.Column(db.String(30))
    b_status = db.Column(db.String(10))
    amt_paid = db.Column(db.Integer)
    
    ordered_food = db.relationship("OrderedFood", back_populates = "booking")
    table = db.relationship("Table")

    def __init__(self, t_id, u_email, b_status, amt_paid):
        self.t_id = t_id
        self.u_email = u_email
        self.b_status = b_status
        self.amt_paid = amt_paid
    
    def json(self):
        return {"b_id":self.b_id, "t_id":self.t_id, "u_email":self.u_email, "b_status":self.b_status, "amt_paid":self.amt_paid}

    @classmethod
    def getjson(cls, booking_list):
        return {'booking_list':[data.json() for data in booking_list]}
    
    @classmethod
    def find_by_b_id(cls, b_id):
        return cls.query.filter_by(b_id=b_id).first()
    
    @classmethod
    def find_by_u_email(cls, u_email):
        #returns list of all bookings made by an user
        return cls.query.filter_by(u_email=u_email).all()