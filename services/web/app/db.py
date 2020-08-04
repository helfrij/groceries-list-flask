import sqlite3
from flask import g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            'groceries_alembic',
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db():
    db = g.pop('db', None)
    if db is not None:
        db.close()


def query_db(sql: str, args=()):
    cursor = get_db().execute(sql, args)
    result = cursor.fetchall()
    cursor.close()
    return result
