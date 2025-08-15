from typing import List
from seed import connect_db

def stream_users_in_batches(batch_size: int):
    connection = connect_db()
    cursor = connection.cursor()

    batch: List = []
    cursor.execute('SELECT * FROM user_data')
    rows = cursor.fetchall()

    for row in rows:
        batch.append(row)
        if len(batch) == batch_size:
            yield batch
            batch = []


def batch_processing(batch_size):
    batched_users = stream_users_in_batches(batch_size)
    
    filtered_users = {users for batch in batched_users for users in batch if users[3]> 25}
    return filtered_users