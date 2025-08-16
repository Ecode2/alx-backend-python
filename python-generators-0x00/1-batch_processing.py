from typing import List
from seed import connect_to_prodev

def stream_users_in_batches(batch_size: int):
    connection = connect_to_prodev()
    cursor = connection.cursor()

    try:
        batch: List = []
        cursor.execute('SELECT * FROM user_data')
        rows = cursor.fetchall()

        for row in rows:
            batch.append(row)
            if len(batch) == batch_size:
                yield batch
                batch = []
    finally:
        cursor.close()
        connection.close()

def batch_processing(batch_size):
    batched_users = stream_users_in_batches(batch_size)

    filtered_users = {users for batch in batched_users for users in batch if users[3]> 25}
    return filtered_users