import sqlite3
from flask_restful import Resource
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser() 
    parser.add_argument('username', 
        type = str, 
        required = True, 
        help = "This field is cannot be blank"
    )
    parser.add_argument('password', 
        type = str, 
        required = True, 
        help = "This field is cannot be blank"
    )
    
    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "This user already exits!"}, 400
        
        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully!"}, 201



class UserList(Resource):
    
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users"
        result = cursor.execute(query)
        rows = result.fetchall()
        users = []
        for row in rows:
            user = {'id': row[0], 'username': row[1], 'password': row[2]}
            users.append(user)

        return {'users': users}, 201