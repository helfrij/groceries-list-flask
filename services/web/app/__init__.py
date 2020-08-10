from flask import Flask
from flask_restful import Api
from app import repository
from app.api import GroceryListsApi, GroceryListApi, GroceryListItemsApi, GroceryListItemApi
from app.db import db
from app.domain import GroceryList, GroceryItem


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    api = Api(app)
    api.add_resource(GroceryListsApi, '/grocery_lists')
    api.add_resource(GroceryListApi, '/grocery_lists/<int:list_id>')
    api.add_resource(GroceryListItemsApi, '/grocery_lists/<int:list_id>/grocery_items')
    api.add_resource(GroceryListItemApi, '/grocery_lists/<int:list_id>/grocery_items/<int:item_id>')

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    return app
