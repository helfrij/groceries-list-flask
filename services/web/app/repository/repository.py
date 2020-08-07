from sqlite3 import Row
from typing import List
from app.db import query_db
from app.domain import GroceryList, GroceryItem


def get_grocery_lists() -> List[GroceryList]:
    grocery_lists_rows = query_db('select * from grocery_lists')
    grocery_items_rows = query_db('select * from grocery_items')
    return _grocery_lists_from_rows(grocery_lists_rows, grocery_items_rows)


def get_grocery_list_by_id(list_id: int) -> GroceryList:
    grocery_list_rows = query_db('select * from grocery_lists where id=%s', [list_id])
    if len(grocery_list_rows) != 1:
        raise GroceryListNotFoundException(list_id)

    grocery_items_rows = query_db('select * from grocery_items where list_id=%s', [list_id])
    return _grocery_list_from_row(grocery_list_rows[0], grocery_items_rows)


def create_grocery_list(name: str) -> GroceryList:
    query_db('insert into grocery_lists (name) values (%s)', [name])
    new_id: int = query_db('select last_insert_rowid()')
    return get_grocery_list_by_id(new_id)


def delete_grocery_list(list_id: int) -> None:
    grocery_list: GroceryList = get_grocery_list_by_id(list_id)
    if grocery_list:
        query_db('delete from grocery_lists where id=%s', [list_id])
        return
    else:
        raise GroceryListNotFoundException(list_id)


def add_grocery_item_to_list(list_id: int, new_item: GroceryItem) -> GroceryList:
    query_db(
        'insert into grocery_items (list_id, name, quantity) values (%s, %s, %s)',
        [list_id, new_item['name'], new_item['quantity']]
    )
    return get_grocery_list_by_id(list_id)


def delete_grocery_item_from_list(list_id: int, item_id: int) -> GroceryList:
    grocery_items_rows = query_db('select * from grocery_items where list_id=%s and id=%s', [list_id, item_id])
    if len(grocery_items_rows) == 1:
        query_db('delete from grocery_items where id=%s and list_id=%s', [item_id, list_id])
    return get_grocery_list_by_id(list_id)


def _grocery_list_from_row(grocery_list_row: Row, grocery_items_rows: List[Row]) -> GroceryList:
    grocery_items_rows_for_list = list(filter(lambda x: x['list_id'] == grocery_list_row['id'], grocery_items_rows))
    grocery_items = list(map(
        lambda x: GroceryItem(id=x['id'], name=x['name'], quantity=x['quantity']),
        grocery_items_rows_for_list
    ))
    return GroceryList(id=grocery_list_row['id'], name=grocery_list_row['name'], items=grocery_items)


def _grocery_lists_from_rows(grocery_list_rows: List[Row], grocery_items_rows: List[Row]) -> List[GroceryList]:
    grocery_lists = [_grocery_list_from_row(grocery_list_row, grocery_items_rows) for grocery_list_row in grocery_list_rows]
    return grocery_lists


class GroceryListNotFoundException(Exception):
    def __init__(self, list_id):
        self.list_id = list_id
