import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self,username,password,database):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user=username,
                password=password,
                database=database
            )
            if conn.is_connected():
                print("Database connection successful")
                self.conn = conn
        except Error as e:
            print(f"Error while connecting to database: {e}")
            exit(1)

