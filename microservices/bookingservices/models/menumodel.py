from db import db

class Menu(db.Model):
    __tablename__ = 'menu'
    f_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    f_name = db.Column(db.String(10))
    r_id = db.Column(db.Integer, db.ForeignKey('restaurants.r_id'))
    f_amt = db.Column(db.Integer)
    
    restaurant = db.relationship("Restaurant")

    def __init__(self, f_name, r_id, f_amt):
        self.f_name = f_name
        self.r_id = r_id
        self.f_amt = f_amt
    
    def json(self):
        return {"f_id":self.f_id,"f_name":self.f_name,"r_id":self.r_id, "f_amt":self.f_amt}
    
    @classmethod
    def getjson(cls, food_list):
        return {'food_list':[data.json() for data in food_list]}
    
    @classmethod
    def find_by_f_id(cls, f_id):
        return cls.query.filter_by(f_id=f_id).first()
    
    @classmethod
    def find_by_r_id(cls, r_id):
        #returns list of all food in a requested restaurant
        return cls.query.filter_by(r_id=r_id).all()