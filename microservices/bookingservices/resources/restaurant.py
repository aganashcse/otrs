import json

from flask_restful import Resource, reqparse
from models.restaurantmodel import Restaurant

class GetRestaurant(Resource):

    def get(self, r_id):
        #Get restaurant by id
        if Restaurant.find_by_id(r_id):
            return Restaurant.find_by_id(r_id).json(), 200

        return {"message": "Restaurant not found."}, 400

class GetRestaurantDetails(Resource):

    def get(self, r_id):
        #Get a restaurant's details
        if Restaurant.find_by_id(r_id):
            result = Restaurant.find_by_id(r_id)
            return {"Restaurant":result.json(), "Menu":Restaurant.getmenujson(result.menu), "Tables":Restaurant.gettablejson(result.tables)}, 200

        return {"message": "Restaurant not found."}, 400

class GetAllRestaurantDetails(Resource):

    def get(self):
        #Get all restaurants details
        if Restaurant.get_all_restaurants():
            return Restaurant.get_all_restaurants().json(), 200

        return {"message": "Restaurant not found."}, 400
