import csv
from typing import List, Tuple
from mysql import connector
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from mysql.connector.pooling import PooledMySQLConnection

def connect_db() -> MySQLConnectionAbstract | PooledMySQLConnection:
    data_base = connector.connect(
        user='e_code',
    )

    return data_base


def create_database(connection: MySQLConnection) -> None:
    cursor: MySQLCursor = connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")


def connect_to_prodev() -> MySQLConnectionAbstract | PooledMySQLConnection: 
    data_base = connector.connect(
        user='e_code',
        database='ALX_prodev',
    )
    
    return data_base


def create_table(connection: MySQLConnection) -> None:
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF EXISTS user_data (
            user_id UUID PRIMARY KEY,
            name VARCHAR NOT NULL,
            email VARCHAR NOT NULL UNIQUE,
            age DECIMAL NOT NULL,
        )""")


def insert_data(connection: MySQLConnection, data: str):
    cursor = connection.cursor()
    cursor.execute("SECECT * FROM user_data")
    user_data = cursor.fetchall()

    if not user_data:
        with open(data, "r") as sample_data:
            csv_data: Tuple = tuple(csv.reader(sample_data))

            cursor.executemany("INSERT INTO user_data (name, email, age) VALUES (%s, %s, %f,)", csv_data[0:])


