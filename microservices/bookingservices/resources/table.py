from flask_restful import Resource, reqparse
from models.tablemodel import Table

class GetTable(Resource):

    def get(self, t_id):
        #Get Table by id
        if Table.find_by_t_id(t_id):
            return Table.find_by_t_id(t_id).json(), 200

        return {"message": "Table not found!."}, 400

class GetTableByCapacity(Resource):

    def get(self, t_capacity):
        #Get Tables for given capacity
        if Table.find_by_t_capacity(t_capacity):
            return Table.getjson(Table.find_by_t_capacity(t_capacity)), 200

        return {"message": "Invalid request"}, 400

class GetTableByRestaurant(Resource):

    def get(self, r_id):
        #Get Tables for given capacity
        if Table.find_by_r_id(r_id):
            return Table.getjson(Table.find_by_r_id(r_id)), 200

        return {"message": "Restaurant not found."}, 400

class GetFreeTables(Resource):

    def get(self):
        #Get all free tables
        if Table.find_by_status():
            return Table.getjson(Table.find_by_status()), 200

        return {"message": "Invalid request"}, 400
