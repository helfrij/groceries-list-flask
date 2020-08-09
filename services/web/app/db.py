import os
import psycopg2


def get_db():
    return psycopg2.connect(
        host=os.environ.get('POSTGRES_HOST'),
        port=os.environ.get('POSTGRES_PORT'),
        dbname=os.environ.get('POSTGRES_DB'),
        user=os.environ.get('POSTGRES_USER'),
        password=os.environ.get('POSTGRES_PASSWORD')
    )


def query_db(sql: str, args=()):
    cursor = get_db().cursor()
    cursor.execute(sql, args)
    result = cursor.fetchall()
    cursor.close()
    return result
