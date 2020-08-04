from flask_restful import reqparse, abort, Resource
from app import repository
from app.domain import GroceryList


parser = reqparse.RequestParser()
parser.add_argument('grocery_list')
parser.add_argument('grocery_item')


class GroceryListsApi(Resource):
    def get(self):
        result = GroceryList.schema().dump(repository.get_grocery_lists(), many=True)
        return {'data': result}

    def post(self):
        args = parser.parse_args()
        result = repository.create_grocery_list(args['grocery_list']).to_dict()
        return {'data': result}, 201


class GroceryListApi(Resource):
    def get(self, list_id: int):
        result = repository.get_grocery_list_by_id(list_id).to_dict()
        return {'data': result}

    def delete(self, list_id: int):
        repository.delete_grocery_list(list_id)
        return {}


class GroceryListItemsApi(Resource):
    def post(self, list_id: int):
        args = parser.parse_args()
        result = repository.add_grocery_item_to_list(list_id, args['grocery_item'])
        return {'data': result}


class GroceryListItemApi(Resource):
    def delete(self, list_id: int, item_id: int):
        repository.delete_grocery_item_from_list(list_id, item_id)
        return {}
