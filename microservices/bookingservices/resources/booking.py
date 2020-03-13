from flask_restful import Resource, reqparse
from models.bookingmodel import Booking

class GetBooking(Resource):

    def get(self, b_id):
        #Get Booking by id
        if Booking.find_by_b_id(b_id):
            return Booking.find_by_b_id(b_id).json(), 200

        return {"message": "Booking not found."}, 400

class GetUserBooking(Resource):

    def get(self, u_email):
        #Get Bookings done by an user
        if Booking.find_by_u_email(u_email):
            return Booking.getjson(Booking.find_by_u_email(u_email)), 200

        return {"message": "Invalid request"}, 400
