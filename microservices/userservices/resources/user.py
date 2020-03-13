from flask_restful import Resource, reqparse
from models.usermodel import User


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('u_email',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('u_passwd',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_email(data['u_email']):
            return {"message": "A user with that username already exists"}, 400

        user = User(data['u_email'], data['u_passwd'])
        user.insert_to_db()
        return {"message": "User created successfully."}, 201

class GetUser(Resource):

    def get(self, u_email):
        if User.find_by_email(u_email):
            return User.find_by_email(u_email).json(), 200

        return {"message": "User email not registered."}, 400