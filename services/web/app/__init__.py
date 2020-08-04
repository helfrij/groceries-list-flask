from flask import Flask
from flask_restful import Api
from app import repository
from app.api import GroceryListsApi, GroceryListApi, GroceryListItemsApi, GroceryListItemApi
from app.config import Config
from app.db import close_db
from app.domain import GroceryList, GroceryItem


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    api = Api(app)
    api.add_resource(GroceryListsApi, '/grocery_lists')
    api.add_resource(GroceryListApi, '/grocery_lists/<int:list_id>')
    api.add_resource(GroceryListItemsApi, '/grocery_lists/<int:list_id>/grocery_items')
    api.add_resource(GroceryListItemApi, '/grocery_lists/<int:list_id>/grocery_items/<int:item_id>')

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    @app.teardown_appcontext
    def shutdown_db_connection(exception=None):
        close_db()

    return app
