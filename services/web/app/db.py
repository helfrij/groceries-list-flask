import psycopg2


def get_db():
    return psycopg2.connect(
        host='localhost',
        dbname='groceries_list_flask',
        user='postgres',
        password='postgres'
    )


def query_db(sql: str, args=()):
    cursor = get_db().cursor()
    cursor.execute(sql, args)
    result = cursor.fetchall()
    cursor.close()
    return result
