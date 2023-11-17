import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        database='inventario_aplicativo_pos'
    )

def close_connection(connection):
    connection.close()

def execute_query(query, values=None, fetchone=False):
    connection = create_connection()
    cursor = connection.cursor(buffered=True)

    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)

        connection.commit()

        if fetchone:
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()

        return result

    finally:
        close_connection(connection)

