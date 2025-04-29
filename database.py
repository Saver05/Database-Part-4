# database.py
import pymysql

def connect_to_database():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="Triforce3!",  # Replace with your actual password
            database="MuskieCo"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        exit(1)

def set_up_database(conn):
    with open("Database.sql", "r") as file:
        sql_script = file.read()
    statements = [stmt.strip() for stmt in sql_script.split(';') if stmt.strip()]

    with conn.cursor() as cursor:
        for stmt in statements:
            try:
                cursor.execute(stmt)
            except Exception as e:
                print(f"Error executing statement: {stmt}\n{e}")

    conn.commit()

def get_input(prompt):
    return input(prompt + ": ")

def add_store(conn, store_address, location):
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO Store (StoreAddress, Location) VALUES (%s, %s)", (store_address, location))
            conn.commit()
            print("Store added successfully.")
    except Exception as e:
        print(f"Error adding store: {e}")

def update_store(conn, store_id, new_address):
    try:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE Store SET StoreAddress = %s WHERE StoreID = %s", (new_address, store_id))
            conn.commit()
            print("Store updated successfully.")
    except Exception as e:
        print(f"Error updating store: {e}")

def delete_store(conn, store_id):
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM Store WHERE StoreID = %s", (store_id,))
            conn.commit()
            print("Store deleted successfully.")
    except Exception as e:
        print(f"Error deleting store: {e}")

def search_store(conn, store_id):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Store WHERE StoreID = %s", (store_id,))
            store = cursor.fetchone()
            if store:
                print(f"StoreID: {store[0]}, Store Address: {store[1]}, Location: {store[2]}")
            else:
                print("Store not found.")
    except Exception as e:
        print(f"Error searching for store: {e}")
