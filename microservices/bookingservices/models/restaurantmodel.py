from db import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    r_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    r_name = db.Column(db.String(15))
    r_address = db.Column(db.String(30))
    
    menu = db.relationship("Menu", back_populates = "restaurant")
    tables = db.relationship("Table", back_populates = "restaurant")

    def __init__(self, r_name, r_address):
        self.r_name = r_name
        self.r_address = r_address
    
    def json(self):
        return {"r_id":self.r_id, "r_name":self.r_name, "r_address":self.r_address}
    
    @classmethod
    def getjson(cls, restaurant_list):
        return {'Restaurant_list':[data.json() for data in restaurant_list]}
    
    @classmethod
    def menujson(cls, menu_obj):
        return {"f_id": menu_obj.f_id,"f_name": menu_obj.f_name, "r_id": menu_obj.r_id, "f_amt": menu_obj.f_amt}
    
    @classmethod
    def getmenujson(cls, menu_list):
        return {'Menu_list':[Restaurant.menujson(data) for data in menu_list]}

    @classmethod
    def tablejson(cls, table_obj):
        return {"t_id": table_obj.t_id,"t_capacity": table_obj.t_capacity, "r_id": table_obj.r_id, "price": table_obj.price, "status": table_obj.status}
    
    @classmethod
    def gettablejson(cls, table_list):
        return {'Table_list':[Restaurant.tablejson(data) for data in table_list]}
    
    @classmethod
    def find_by_id(cls, r_id):
        return cls.query.filter_by(r_id=r_id).first()
    
    @classmethod
    def get_all_restaurants(cls):
        #returns list of all restaurants
        return cls.query.order_by(Restaurant.r_id).all()