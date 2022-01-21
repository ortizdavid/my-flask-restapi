import sqlite3
from flask_restful import Resource
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.item import ItemModel


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be blank!"
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
           return item.json()
        return {"message": "Item not found"}, 404

    def post(self, name):
       
        if ItemModel.find_by_name(name):
            return {'message': "The item '{}' already exists".format(name)}
        
        data = Item.parser.parse_args()
        item =  ItemModel(name, data['price'])

        try:
            item.insert()
        except:
            return {"message": "An error occored inserting"}

        return item.json(), 201

   # @jwt_required()
    def delete(self, name):
        item = Item.find_by_name(name)
        if item:
            item.delete_from_db()
        
        return {'message': 'Item Deleted'}

    def put(self, name):

        data = Item.parser.parse_args()
        item =  ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data['price'])  
        else:
            item.price = data['price']

        item.save_to_db()

        return item.json(), 201


class ItemList(Resource):

    def get(self):
        #items = list(map(lambda x: x.json(), ItemModel.find_all()))
        items = [item.json() for item in ItemModel.find_all()]
        return {'items': items}

