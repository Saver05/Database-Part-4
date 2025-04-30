# database.py - Contains all database operations for the MuskieCo management system
import pymysql

def connect_to_database():
    """
    Establishes a connection to the MuskieCo database.
    
    Returns:
        pymysql.connections.Connection: A connection to the database if successful.
        
    Raises:
        Exception: If connection fails, the program will exit with error code 1.
    """
    try:
        # Connect to MySQL database using pymysql driver
        # The database is configured in docker-compose.yml with the same credentials
        conn = pymysql.connect(
            host="127.0.0.1",  # localhost or container name
            user="root",  # default MySQL username
            password="Triforce3!",  # Replace with your actual password
            database="MuskieCo",  # database name
            port=3306  # standard MySQL port
        )
        # Set up database schema if not already done
        set_up_database(conn)
        return conn
    except Exception as e:
        # Print error and exit if connection fails
        print(f"Error connecting to database: {e}")
        exit(1)

def set_up_database(conn):
    """
    Sets up the database schema by executing SQL statements from the Database.sql file.
    
    Args:
        conn (pymysql.connections.Connection): The database connection.
    """
    # Read SQL commands from external file
    with open("Database.sql", "r") as file:
        sql_script = file.read()
    # Split SQL script into individual statements
    statements = [stmt.strip() for stmt in sql_script.split(';') if stmt.strip()]

    # Execute each statement separately
    with conn.cursor() as cursor:
        for stmt in statements:
            try:
                cursor.execute(stmt)
            except Exception as e:
                # Continue even if some statements fail (might be because tables already exist)
                print(f"Error executing statement: {stmt}\n{e}")

    # Commit changes to the database
    conn.commit()

def get_input(prompt):
    """
    Gets user input with a formatted prompt.
    
    Args:
        prompt (str): The prompt message to display to the user.
        
    Returns:
        str: The user's input.
    """
    # Format input prompt with a colon and space for consistency
    return input(prompt + ": ")


def add_store(conn, store_address, phone_number, manager_id):
    """
    Adds a new store to the database.
    
    Args:
        conn (pymysql.connections.Connection): The database connection.
        store_address (str): The address of the store.
        phone_number (str): The phone number of the store.
        manager_id (str): The ID of the store manager.
    """
    try:
        with conn.cursor() as cursor:
            # Using parameterized query to prevent SQL injection
            cursor.execute("INSERT INTO Store (StoreAddress, PhoneNumber, ManagerID) VALUES (%s, %s, %s)",
                           (store_address, phone_number, manager_id))
            # Save changes to the database
            conn.commit()
            print("Store added successfully.")
    except Exception as e:
        # Handle errors during store addition
        print(f"Error adding store: {e}")


def update_store(conn, store_id, address, phone_number, manager_id):
    """
    Updates an existing store in the database.
    
    Args:
        conn (pymysql.connections.Connection): The database connection.
        store_id (int): The ID of the store to update.
        address (str): The new address of the store.
        phone_number (str): The new phone number of the store.
        manager_id (str): The new ID of the store manager.
    """
    try:
        with conn.cursor() as cursor:
            # Update all store fields with new values
            cursor.execute(
                "UPDATE Store SET StoreAddress = %s, PhoneNumber = %s, ManagerID = %s WHERE StoreID = %s",
                (address, phone_number, manager_id, store_id))
            # Save changes to the database
            conn.commit()
            print("Store updated successfully.")
            # Display the updated store information
            print(search_store(conn, store_id))
    except Exception as e:
        # Handle errors during store update
        print(f"Error updating store: {e}")

def delete_store(conn, store_id):
    """
    Deletes a store from the database.
    
    Args:
        conn (pymysql.connections.Connection): The database connection.
        store_id (int): The ID of the store to delete.
    """
    try:
        with conn.cursor() as cursor:
            # Delete store with the given ID
            # Note: This may fail if there are products or other records referencing this store
            cursor.execute("DELETE FROM Store WHERE StoreID = %s", (store_id,))
            # Save changes to the database
            conn.commit()
            print("Store deleted successfully.")
    except Exception as e:
        # Handle errors during store deletion
        print(f"Error deleting store: {e}")

def search_store(conn, store_id):
    """
    Searches for a store by its ID.
    
    Args:
        conn (pymysql.connections.Connection): The database connection.
        store_id (int): The ID of the store to search for.
        
    Returns:
        tuple: The store information if found, None otherwise.
    """
    try:
        with conn.cursor() as cursor:
            # Search for store with the given ID
            cursor.execute("SELECT * FROM Store WHERE StoreID = %s", (store_id,))
            # Fetch the first matching record
            store = cursor.fetchone()
            if store:
                # Display store information if found
                # store[0] = StoreID, store[1] = ManagerID, store[2] = StoreAddress, store[3] = PhoneNumber
                print(f"StoreID: {store[0]}, ManagerID: {store[1]} ,Store Address: {store[2]}, PhoneNumber: {store[3]}")
                return store
            else:
                # If no store is found with the given ID
                print("Store not found.")
                return None
    except Exception as e:
        # Handle errors during store search
        print(f"Error searching for store: {e}")
        return None


def add_product(conn, product_id, product_name, QuantityInStock, BuyPrice, SellPrice, StoreID):
    """
    Adds a new product to the database.
    
    Args:
        conn (pymysql.connections.Connection): The database connection.
        product_id (str): The ID of the product.
        product_name (str): The name of the product.
        QuantityInStock (int): The quantity of the product in stock.
        BuyPrice (float): The buy price of the product.
        SellPrice (float): The sell price of the product.
        StoreID (int): The ID of the store where the product is located.
    """
    try:
        with conn.cursor() as cursor:
            # Insert new product with all required fields
            cursor.execute(
                "INSERT INTO Product (ProductID, ProductName, QuantityInStock, BuyPrice, SellPrice, StoreID) VALUES (%s, %s, %s, %s, %s, %s)",
                (product_id, product_name, QuantityInStock, BuyPrice, SellPrice, StoreID))
            # Save changes to the database
            conn.commit()
            print("Product added successfully.")
            # Display the newly added product
            print(get_product(conn, product_id))
    except Exception as e:
        # Handle errors during product addition
        print(f"Error adding product: {e}")


def get_product(conn, product_id):
    """
    Retrieves a product by its ID.
    
    Args:
        conn (pymysql.connections.Connection): The database connection.
        product_id (str): The ID of the product to retrieve.
        
    Returns:
        tuple: The product information if found, None otherwise.
    """
    try:
        with conn.cursor() as cursor:
            # Search for product with the given ID
            cursor.execute("SELECT * FROM Product WHERE ProductID = %s", (product_id,))
            # Fetch the first matching record
            product = cursor.fetchone()
            if product:
                # Display product information if found
                # product[0] = ProductID, product[1] = ProductName, product[2] = QuantityInStock,
                # product[3] = BuyPrice, product[4] = SellPrice, product[5] = StoreID
                print(
                    f"ProductID: {product[0]}, Product Name: {product[1]}, Quantity In Stock: {product[2]}, Buy Price: {product[3]}, Sell Price: {product[4]}, StoreID: {product[5]}")
                return product
            else:
                # If no product is found with the given ID
                print("Product not found.")
                return None

    except Exception as e:
        # Handle errors during product retrieval
        print(f"Error getting product: {e}")
        return None


def update_product(conn, product_id, product_name, QuantityInStock, BuyPrice, SellPrice, StoreID):
    """
    Updates an existing product in the database.
    
    Args:
        conn (pymysql.connections.Connection): The database connection.
        product_id (str): The ID of the product to update.
        product_name (str): The new name of the product.
        QuantityInStock (int): The new quantity of the product in stock.
        BuyPrice (float): The new buy price of the product.
        SellPrice (float): The new sell price of the product.
        StoreID (int): The new ID of the store where the product is located.
    """
    try:
        with conn.cursor() as cursor:
            # Update all product fields with new values
            cursor.execute(
                "UPDATE Product SET ProductName = %s, QuantityInStock = %s, BuyPrice = %s, SellPrice = %s, StoreID = %s WHERE ProductID = %s",
                (product_name, QuantityInStock, BuyPrice, SellPrice, StoreID, product_id))
            # Save changes to the database
            conn.commit()
            print("Product updated successfully.")
            # Display the updated product information
            print(get_product(conn, product_id))
    except Exception as e:
        # Handle errors during product update
        print(f"Error updating product: {e}")


def delete_product(conn, product_id):
    """
    Deletes a product from the database.
    
    Args:
        conn (pymysql.connections.Connection): The database connection.
        product_id (str): The ID of the product to delete.
    """
    try:
        with conn.cursor() as cursor:
            # Delete product with the given ID
            cursor.execute("DELETE FROM Product WHERE ProductID = %s", (product_id,))
            # Save changes to the database
            conn.commit()
            print("Product deleted successfully.")
    except Exception as e:
        # Handle errors during product deletion
        print(f"Error deleting product: {e}")
