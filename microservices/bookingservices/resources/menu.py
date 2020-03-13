from flask_restful import Resource, reqparse
from models.menumodel import Menu

class GetFood(Resource):

    def get(self, f_id):
        #Get food by food_id
        if Menu.find_by_f_id(f_id):
            return Menu.find_by_f_id(f_id).json(), 200

        return {"message": "Food not found!."}, 400

class GetMenu(Resource):

    def get(self, r_id):
        #Get menu in a restaurant
        if Menu.find_by_r_id(r_id):
            return Menu.getjson(Menu.find_by_r_id(r_id)), 200

        return {"message": "Menu didn't found in this restaurant."}, 400
