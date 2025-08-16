from seed import connect_to_prodev


def stream_user_ages():
    connection = connect_to_prodev()
    cursor = connection.cursor()
    
    try:
        cursor.execute('SELECT age FROM user_data')
        users_age = cursor.fetchall()

        for age in users_age:
            yield age[0]
    finally:
        cursor.close()
        connection.close()


def print_average():
    age = stream_user_ages()
    total_age = 0
    count = 0

    for user_age in age:
        total_age += user_age
        count += 1

        average_age = total_age / count if count > 0 else 0
        print(f"Average age of users: {average_age:.2f}")
    
    
    if __name__ == "__main__":
        print_average()
