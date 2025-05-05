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
            port=3307  # standard MySQL port
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

def add_transaction(conn, storeid, customerid, cashierid, purchasedate, totalprice, transactiontype):
    """
    Adds a new transaction to the database.
    
    Args:
        conn (pymysql.connections.Connection): The database connection.
        storeid (int): The ID of the store where the transaction took place.
        customerid (int): The ID of the customer who made the transaction.
        cashierid (int): The ID of the cashier who processed the transaction.
        purchasedate (date): The date when the transaction occurred.
        totalprice (float): The total price of the transaction.
        transactiontype (str): The type of transaction ('Buy' or 'Return').
        
    Returns:
        int: The ID of the newly created transaction if successful, None otherwise.
    """
    try:
        with conn.cursor() as cursor:
            # Insert new transaction with all required fields using parameterized query
            cursor.execute("INSERT INTO Transaction (StoreID, CustomerID, CashierID, PurchaseDate, TotalPrice, TransactionType) VALUES (%s, %s, %s, %s, %s, %s)",
                          (storeid, customerid, cashierid, purchasedate, totalprice, transactiontype))
            # Get the ID of the newly inserted transaction
            transaction_id = cursor.lastrowid
            # Save changes to the database
            conn.commit()
            print("Transaction added successfully.")
            return transaction_id
    except Exception as e:
        # Handle errors during transaction addition
        print(f"Error adding transaction: {e}")
        return None

def get_transaction(conn, transaction_id):
    """
    Retrieves a transaction and its associated products by transaction ID.
    
    Args:
        conn (pymysql.connections.Connection): The database connection.
        transaction_id (int): The ID of the transaction to retrieve.
        
    Returns:
        tuple: The transaction information if found, None otherwise.
              Note: This function currently returns None in all cases.
    """
    try:
        with conn.cursor() as cursor:
            # Query the Transaction table for the main transaction details
            cursor.execute("Select * from Transaction where TransactionID = %s", (transaction_id,))
            transaction = cursor.fetchone()
            
            # Query the ProductTransaction table for all products in this transaction
            cursor.execute("Select * from TransactionItem where TransactionID = %s", (transaction_id,))
            products = cursor.fetchall()
            
            if transaction:
                # Display transaction and associated product details if found
                print(transaction)
                print(products)
                return None
            else:
                # If no transaction is found with the given ID
                print("Transaction not found.")
                return None
    except Exception as e:
        # Handle errors during transaction retrieval
        print(f"Error getting transaction: {e}")
        return None

def add_products_to_transaction(conn, transaction_id, product_entries):
    """
    Adds multiple products to an existing transaction.
    
    Args:
        conn (pymysql.connections.Connection): The database connection.
        transaction_id (int): The ID of the transaction to add products to.
        product_entries (list): A list of dictionaries, where each dictionary contains:
            - product_id (str/int): The ID of the product.
            - quantity (int): The quantity of the product.
            - discount (float): The discount percentage applied to the product.
    
    Returns:
        None
    """
    try:
        with conn.cursor() as cursor:
            # Begin transaction manually to ensure atomicity
            conn.begin()

            # Display existing transaction details before changes
            get_transaction(conn, transaction_id)

            # Insert each product into the ProductTransaction table
            for product in product_entries:
                # Extract product details from the dictionary
                product_id = product['product_id']
                quantity = product['quantity']
                discount = product['discount']
                
                # Insert the product into the transaction with parameterized query
                cursor.execute(
                    """
                    INSERT INTO ProductTransaction (TransactionID, ProductID, Quantity, DiscountPercentageApplied)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (transaction_id, product_id, quantity, discount)
                )

            # Commit the transaction after all inserts are successful
            conn.commit()
            print("All products added successfully.")
            
            # Display updated transaction details
            get_transaction(conn, transaction_id)

    except Exception as e:
        # Rollback all changes if any error occurs to maintain data integrity
        conn.rollback()  # Rollback on error
        print(f"Error adding products to transaction: {e}")


def get_transaction_price(conn, transaction_id):
    """
    Calculates the total price of a transaction based on its product items.
    
    Args:
        conn (pymysql.connections.Connection): The database connection.
        transaction_id (int): The ID of the transaction to calculate price for.
        
    Returns:
        float: The total price of the transaction if calculation is successful,
               None otherwise.
    """
    try:
        with conn.cursor() as cursor:
            # Get all products in the transaction and their quantities
            cursor.execute("Select ProductID, Quantity from TransactionItem where TransactionID = %s", (transaction_id,))
            products = cursor.fetchall()
            
            # Initialize total price counter
            total_price = 0
            
            # Calculate total price by summing (product price × quantity) for each product
            for product in products:
                product_id = product[0]
                quantity = product[1]
                
                # Get product details to access the sell price
                product_info = get_product(conn, product_id)
                sell_price = product_info[4]  # Index 4 contains the SellPrice
                
                # Add this product's contribution to the total price
                total_price += sell_price * quantity
                
            return total_price
    except Exception as e:
        # Handle errors during price calculation
        print(f"Error getting transaction price: {e}")
        return None

def get_customer(conn, customer_id):
    """
    Retrieves a customer by their ID.
    
    Args:
        conn (pymysql.connections.Connection): The database connection.
        customer_id (int): The ID of the customer to retrieve.
        
    Returns:
        tuple: The customer information if found, None otherwise.
    """
    try:
        with conn.cursor() as cursor:
            # Search for customer with the given ID using parameterized query
            cursor.execute("Select * from Customer where CustomerID = %s", (customer_id,))
            
            # Fetch the first matching record
            customer = cursor.fetchone()
            
            if customer:
                # Display customer information if found
                # customer contains: CustomerID, FirstName, LastName, Email, PhoneNumber, etc.
                print(customer)
                return customer
            else:
                # If no customer is found with the given ID
                print("Customer not found.")
                return None
    except Exception as e:
        # Handle errors during customer retrieval
        print(f"Error getting customer: {e}")
        return None

def get_transactions_month(conn, customer_id, month):
    """
    Retrieves all transactions for a specific customer during a specific month.
    
    Args:
        conn (pymysql.connections.Connection): The database connection.
        customer_id (int): The ID of the customer to retrieve transactions for.
        month (int): The month number (1-12) to filter transactions by.
        
    Returns:
        list: A list of transactions if found, None otherwise.
    """
    try:
        with conn.cursor() as cursor:
            # Search for transactions with the given customer ID and month
            # using MySQL's MONTH() function and parameterized query
            cursor.execute("Select * from Transaction where CustomerID = %s and Month(PurchaseDate) = %s", 
                          (customer_id, month))
            
            # Fetch all matching transactions
            transactions = cursor.fetchall()
            
            if transactions:
                # Display transaction information if found
                print(transactions)
                return transactions
            else:
                # If no transactions are found for the customer in the specified month
                print("No transactions not found.")
                return None
    except Exception as e:
        # Handle errors during transactions retrieval
        print(f"Error getting transactions: {e}")
        return None


def get_monthly_sales_report(conn, store_id, year, month):
    """
    Generates a monthly sales report for a specific store and time period.
    
    This function retrieves and summarizes sales data for a specified store during
    a particular month and year. It calculates the total number of transactions
    and the total sales amount for the given period.
    
    Args:
        conn (pymysql.connections.Connection): The database connection.
        store_id (int): The ID of the store to generate the report for.
        year (str/int): The year (YYYY format) to filter transactions by.
        month (str/int): The month (MM format) to filter transactions by.
        
    Returns:
        list: A list of tuples containing transaction summary data if found:
             - First tuple element: Total number of transactions
             - Second tuple element: Total sales amount
             Returns None if no transactions are found or if an error occurs.
             
    Note:
        The function prints the results to the console in addition to returning them.
        If no sales data is found, it prints a notification message.
    """
    try:
        with conn.cursor() as cursor:
            # Get total sales and transaction count
            cursor.execute(
                """
                SELECT COUNT(*)        as TotalTransactions,
                       SUM(TotalPrice) as TotalSales
                FROM Transaction
                WHERE StoreID = %s and Year(PurchaseDate) = %s and Month(PurchaseDate) = %s
                """,
                (store_id, year, month)
            )

            transactions = cursor.fetchall()
            if transactions:
                print(transactions)
                return transactions
            else:
                print(f"No sales data found for store {store_id} in {year}:{month}")
                return None

    except Exception as e:
        print(f"Error generating monthly sales report: {e}")
        return None


def get_day_sales_report(conn, store_id, date):
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                Select *
                FROM Transaction
                         JOIN TransactionItem On Transaction.TransactionID = TransactionItem.TransactionID
                WHERE Transaction.StoreID = %s and Transaction.PurchaseDate = %s
                """,
                (store_id, date)
            )
            # Fetch all matching sales records
            transactions = cursor.fetchall()

            if transactions:
                # Display sales report information if found
                print(transactions)
                return transactions
            else:
                # If no transactions are found for the store in the specified year
                print("No transactions not found.")
                return None
    except Exception as e:
        # Handle errors during sales report generation
        print(f"Error getting sales report: {e}")
        return None

def get_sales_report_year(conn, store_id, year):
    """
    Generates a sales report for a specific store and year.
    
    Args:
        conn (pymysql.connections.Connection): The database connection.
        store_id (int): The ID of the store to generate the report for.
        year (int): The year to filter transactions by.
        
    Returns:
        list: A list of transactions and their items if found, None otherwise.
    """
    try:
        with conn.cursor() as cursor:
            # Join Transaction and TransactionItem tables to get complete sales information
            # Filter by store ID and year using MySQL's YEAR() function
            cursor.execute(
                """
                Select * FROM Transaction 
                JOIN TransactionItem On Transaction.TransactionID = TransactionItem.TransactionID 
                WHERE Transaction.StoreID = %s and Year(Transaction.PurchaseDate) = %s
                """, 
                (store_id, year)
            )
            
            # Fetch all matching sales records
            transactions = cursor.fetchall()
            
            if transactions:
                # Display sales report information if found
                print(transactions)
                return transactions
            else:
                # If no transactions are found for the store in the specified year
                print("No transactions not found.")
                return None
    except Exception as e:
        # Handle errors during sales report generation
        print(f"Error getting sales report: {e}")
        return None

def get_all_products_quantity(conn, store_id):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT ProductName, QuantityInStock FROM Product WHERE StoreID = %s", (store_id,))
            products = cursor.fetchall()
            print(products)
            return products
    except Exception as e:
        print(f"Error getting all products quantity: {e}")
        return None

def get_products_quantity(conn, store_id, product_ids):
    """
    Retrieves the quantity information for specific products in a store.
    
    Args:
        conn (pymysql.connections.Connection): The database connection.
        store_id (int): The ID of the store to check product quantities in.
        product_ids (list): A list of product IDs to retrieve quantity information for.
        
    Returns:
        list: A list of tuples containing product information if found, None otherwise.
              Each tuple contains (ProductID, ProductName, QuantityInStock).
    """
    try:
        with conn.cursor() as cursor:
            # Dynamically create a parameterized query with the correct number of placeholders
            # for the variable number of product IDs
            format_strings = ','.join(['%s'] * len(product_ids))
            
            # Build the query to get product information for specific products in a store
            query = f"""
                SELECT ProductID, ProductName, QuantityInStock
                FROM Product
                WHERE StoreID = %s AND ProductID IN ({format_strings})
            """
            
            # Execute the query with store_id as the first parameter followed by all product_ids
            cursor.execute(query, [store_id] + product_ids)
            
            # Fetch all matching products
            products = cursor.fetchall()
            
            if products:
                # Display product information if found
                for prod in products:
                    print(f"ProductID: {prod[0]}, Name: {prod[1]}, QuantityInStock: {prod[2]}")
                return products
            else:
                # If no matching products are found
                print("No matching products found.")
                return None
    except Exception as e:
        # Handle errors during product retrieval
        print(f"Error retrieving products: {e}")
        return None