from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine.result import ResultProxy


db = SQLAlchemy()


def query_db(sql: str, args=()) -> ResultProxy:
    session = db.session()
    return session.execute(sql, args)
