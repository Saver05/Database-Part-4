# database.py
import pymysql

def connect_to_database():
    try:
        conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="Triforce3!",  # Replace with your actual password
            database="MuskieCo",
            port=3306
        )
        set_up_database(conn)
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


def add_store(conn, store_address, phone_number, manager_id):
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO Store (StoreAddress, PhoneNumber, ManagerID) VALUES (%s, %s, %s)",
                           (store_address, phone_number, manager_id))
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


def add_product(conn, product_id, product_name, QuantityInStock, BuyPrice, SellPrice, StoreID):
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Product (ProductID, ProductName, QuantityInStock, BuyPrice, SellPrice, StoreID) VALUES (%s, %s, %s, %s, %s, %s)",
                (product_id, product_name, QuantityInStock, BuyPrice, SellPrice, StoreID))
            conn.commit()
            print("Product added successfully.")
            print(get_product(conn, product_id))
    except Exception as e:
        print(f"Error adding product: {e}")


def get_product(conn, product_id):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Product WHERE ProductID = %s", (product_id,))
            product = cursor.fetchone()
            if product:
                print(
                    f"ProductID: {product[0]}, Product Name: {product[1]}, Quantity In Stock: {product[2]}, Buy Price: {product[3]}, Sell Price: {product[4]}, StoreID: {product[5]}")
            else:
                print("Product not found.")
            return product
    except Exception as e:
        print(f"Error getting product: {e}")


def update_product(conn, product_id, product_name, QuantityInStock, BuyPrice, SellPrice, StoreID):
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE Product SET ProductName = %s, QuantityInStock = %s, BuyPrice = %s, SellPrice = %s, StoreID = %s WHERE ProductID = %s",
                (product_name, QuantityInStock, BuyPrice, SellPrice, StoreID, product_id))
            conn.commit()
            print("Product updated successfully.")
            print(get_product(conn, product_id))
    except Exception as e:
        print(f"Error updating product: {e}")


def delete_product(conn, product_id):
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM Product WHERE ProductID = %s", (product_id,))
            conn.commit()
            print("Product deleted successfully.")
    except Exception as e:
        print(f"Error deleting product: {e}")
