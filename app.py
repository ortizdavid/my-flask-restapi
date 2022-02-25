from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
import os

from security import authenticate, identity
from resources.user import UserList, UserRegister
from resources.item import Item, ItemList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgres://rypfziofwofqkb:e263885be862e8eabe2ae1da237168ee4c3d3ca44eb393e481a6b511b1ab300e@ec2-35-175-68-90.compute-1.amazonaws.com:5432/d8g5ettirsctco')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'ortiz'


api = Api(app)
jwt = JWT(app, authenticate, identity)
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserList, '/users')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)