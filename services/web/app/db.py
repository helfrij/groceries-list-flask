from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def query_db(sql: str, args=()):
    session = db.session()
    return session.execute(sql, args)
