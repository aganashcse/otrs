from flask_restful import Resource, reqparse
from models.orderedfoodmodel import OrderedFood

class GetOrderedFood(Resource):

    def get(self, order_id):
        #Get Ordered food by id
        if OrderedFood.find_by_order_id(order_id):
            return OrderedFood.find_by_order_id(order_id).json(), 200

        return {"message": "Order not found."}, 400

class GetAllFoodOrdered(Resource):

    def get(self, b_id):
        #Get all food ordered for given booking
        if OrderedFood.find_by_b_id(b_id):
            return OrderedFood.getjson(OrderedFood.find_by_b_id(b_id)), 200

        return {"message": "Booking not found"}, 400
