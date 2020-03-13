from flask import Flask
from flask_restful import Api

from resources.booking import GetBooking, GetUserBooking
from resources.menu import GetFood, GetMenu
from resources.orderedfood import GetOrderedFood, GetAllFoodOrdered
from resources.restaurant import GetRestaurant, GetRestaurantDetails, GetAllRestaurantDetails
from resources.table import GetTable, GetTableByCapacity, GetTableByRestaurant, GetFreeTables

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1117@0.0.0.0/orts1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'ganesha'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(GetBooking, '/getbooking/<string:b_id>')
api.add_resource(GetUserBooking, '/getuserbooking/<string:u_email>')
api.add_resource(GetFood, '/getfood/<string:f_id>')
api.add_resource(GetMenu, '/getmenu/<string:r_id>')
api.add_resource(GetOrderedFood, '/getorderedfood/<string:order_id>')
api.add_resource(GetAllFoodOrdered, '/getallfoodordered/<string:b_id>')
api.add_resource(GetRestaurant, '/getrestaurant/<string:r_id>')
api.add_resource(GetRestaurantDetails, '/getrestaurantdetails/<string:r_id>')
api.add_resource(GetAllRestaurantDetails, '/getallrestaurantdetails')
api.add_resource(GetTable, '/gettable/<string:t_id>')
api.add_resource(GetTableByCapacity, '/gettablebycapacity/<string:t_capacity>')
api.add_resource(GetTableByRestaurant, '/gettablebyrestaurant/<string:r_id>')
api.add_resource(GetFreeTables, '/getfreetables')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=3333, debug=True)