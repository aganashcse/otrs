from db import db

class Table(db.Model):
    __tablename__ = 'tables'
    t_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    t_capacity = db.Column(db.Integer)
    r_id = db.Column(db.Integer, db.ForeignKey('restaurants.r_id'))
    price = db.Column(db.Integer)
    status = db.Column(db.String(10))
    
    bookings = db.relationship("Booking", back_populates = "table")
    restaurant = db.relationship("Restaurant")

    def __init__(self, t_capacity, r_id, price, status):
        self.t_capacity = t_capacity
        self.r_id = r_id
        self.price = price
        self.status = status
    
    def json(self):
        return {"t_id":self.t_id, "t_capacity":self.t_capacity, "r_id":self.r_id, "r_id":self.r_id, "price":self.price, "status":self.status}
    
    @classmethod
    def getjson(cls, table_list):
        return {'table_list':[data.json() for data in table_list]}

    @classmethod
    def find_by_t_id(cls, t_id):
        return cls.query.filter_by(t_id=t_id).first()
    
    @classmethod
    def find_by_t_capacity(cls, t_capacity):
        #returns list of all restaurant's table with given capacity
        return cls.query.filter_by(t_capacity=t_capacity).all()
    
    @classmethod
    def find_by_r_id(cls, r_id):
        #returns list of all tables in a given restaurant
        return cls.query.filter_by(r_id=r_id).all()
        
    @classmethod
    def find_by_status(cls, status='free'):
        #returns list of all tables with given status(free/booked)
        return cls.query.filter_by(status=status).all()