from seed import connect_db

def stream_users():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM user_data')
    rows = cursor.fetchall()
    for row in rows:
        yield row
    cursor.close()
    connection.close()