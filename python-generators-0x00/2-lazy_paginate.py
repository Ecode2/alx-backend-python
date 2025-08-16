from seed  import connect_to_prodev

def paginate_users(page_size, offset):
    connection = connect_to_prodev()
    cursor = connection.cursor()
    
    try:
        cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
        rows = cursor.fetchall()
    finally:
        connection.close()

    return rows

def lazy_paginate(page_size):
    offset = 0
    while True:
        users = paginate_users(page_size, offset)
        if not users:
            break
        for user in users:
            yield user
        offset += page_size
