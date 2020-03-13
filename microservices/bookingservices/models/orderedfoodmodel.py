from db import db

class OrderedFood(db.Model):
    __tablename__ = 'orderedfood'
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    b_id = db.Column(db.Integer, db.ForeignKey('bookings.b_id'))
    f_id = db.Column(db.Integer, db.ForeignKey('menu.f_id'))
    
    booking = db.relationship("Booking")
    food = db.relationship("Menu")

    def __init__(self, b_id, f_id):
        self.b_id = b_id
        self.f_id = f_id
    
    def json(self):
        return {"order_id":self.order_id, "b_id":self.b_id, "f_id":self.f_id}
    
    @classmethod
    def getjson(cls, ordered_food_list):
        return {'ordered_food_list':[data.json() for data in ordered_food_list]}
    
    @classmethod
    def find_by_order_id(cls, order_id):
        return cls.query.filter_by(order_id=order_id).first()

    @classmethod
    def find_by_b_id(cls, b_id):
        #returns list of all food ordered in a given booking
        return cls.query.filter_by(b_id=b_id).all()