

"""
Customer management module for MuskieCo retail management system.

This module provides functions to perform CRUD operations on customer data,
including adding new customers, updating existing customer information,
deleting customers, and searching for customer records in the database.
"""

def customer(conn):
    """
    Main customer management function that presents a menu-driven interface 
    for managing customer data.
    
    Args:
        conn: Database connection object used for executing SQL queries
        
    The function provides four main operations:
    1. Add a new customer with all required information
    2. Update an existing customer's information
    3. Delete a customer from the database
    4. Find and display customer information
    """
    # Display customer management menu options
    print("1. Add Customer")
    print("2. Update Customer")
    print("3. Delete Customer")
    print("4. Find Customer")
    choice = input("Enter the number corresponding to your choice: ")
    
    # Process user choice using Python 3.10+ pattern matching
    match choice:
        # Option 1: Add a new customer to the database
        case "1":
            # Collect all required customer information through user input
            CustomerID = int(input("Enter Customer ID: "))
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            phonenumber = input("Enter phone number: ")
            homeaddress = input("Enter home address: ")
            # Set default values for new customers
            isActive = True  # New customers are active by default
            signupdate = input("Enter date of signup (YYYY-MM-DD): ")
            rewardspoints = 0  # New customers start with 0 reward points
            
            # Call the create_customer function with all collected information
            create_customer(conn, CustomerID, first_name, last_name, email, phonenumber, 
                           homeaddress, isActive, signupdate, rewardspoints)
            
        # Option 2: Update an existing customer's information
        case "2":
            # Search for the customer by ID before updating
            customer_data = search_customer(conn, int(input("Enter Customer ID: ")))
            
            # If no customer found, display message and return to main menu
            if not customer_data:
                print("No Customer found")
                return
                
            # Convert the customer tuple to a list for easier modification
            customer = list(customer_data)
            
            # Display update options submenu
            print("What would you like to update?")
            print("1. First Name")
            print("2. Last Name")
            print("3. Email")
            print("4. Phone Number")
            print("5. Home Address")
            print("6. Is Active")
            print("7. Signup Date")
            print("8. Reward Points")
            choice = input("Enter choice: ")
            
            # Process the update choice using pattern matching
            match choice:
                # Update specific customer fields based on user selection
                # customer[0] = CustomerID, customer[1] = FirstName, etc.
                case "1":
                    customer[1] = input("Enter new first name: ")
                case "2":
                    customer[2] = input("Enter new last name: ")
                case "3":
                    customer[3] = input("Enter new email: ")
                case "4":
                    customer[4] = input("Enter new phone number: ")
                case "5":
                    customer[5] = input("Enter new home address: ")
                case "6":
                    # Convert string input to boolean for active status
                    customer[6] = True if input("Enter 'True' to activate, 'False' to deactivate: ") == "True" else False
                case "7":
                    customer[7] = input("Enter new signup date (YYYY-MM-DD): ")
                case "8":
                    customer[8] = int(input("Enter new reward points: "))
            
            # Call update_customer with all customer data (modified and unmodified)
            update_customer(conn, customer[0], customer[1], customer[2], customer[3], 
                           customer[4], customer[5], customer[6], customer[7], customer[8])
            
        # Option 3: Delete a customer from the database
        case "3":
            # Get customer ID and call delete function
            delete_customer(conn, int(input("Enter Customer ID: ")))
            
        # Option 4: Find and display customer information
        case "4":
            # Get customer ID and call search function
            search_customer(conn, int(input("Enter Customer ID: ")))

def update_customer(conn, CustomerID, first_name, last_name, email, phonenumber, homeaddress, isActive, signupdate, rewardspoints):
    """
    Updates an existing customer's information in the database.
    
    Args:
        conn: Database connection object
        CustomerID: Unique identifier for the customer (primary key)
        first_name: Customer's first name
        last_name: Customer's last name
        email: Customer's email address
        phonenumber: Customer's phone number
        homeaddress: Customer's home address
        isActive: Boolean indicating if the customer account is active
        signupdate: Date when the customer signed up (YYYY-MM-DD format)
        rewardspoints: Integer representing customer's accumulated reward points
        
    Returns:
        None: Displays success or error message
    """
    try:
        # Use a cursor to execute the SQL UPDATE statement
        with conn.cursor() as cursor:
            # Prepare SQL statement with placeholders for safe parameter insertion
            cursor.execute("UPDATE Customer SET FirstName = %s, LastName = %s, Email = %s, PhoneNumber = %s, HomeAddress = %s, IsActive = %s, SignUpdate = %s, RewardPoints = %s WHERE CustomerID = %s",
                           (first_name, last_name, email, phonenumber, homeaddress, isActive, signupdate, rewardspoints, CustomerID))
            # Commit the transaction to save changes to the database
            conn.commit()
            print("Customer updated successfully.")
    except Exception as e:
        # Catch and display any errors that occur during the update
        print(f"Error updating customer: {e}")

def delete_customer(conn, CustomerID):
    """
    Deletes a customer from the database based on CustomerID.
    
    Args:
        conn: Database connection object
        CustomerID: Unique identifier for the customer to delete
        
    Returns:
        None: Displays success or error message
    """
    try:
        # Use a cursor to execute the SQL DELETE statement
        with conn.cursor() as cursor:
            # Prepare SQL statement with placeholder for CustomerID
            cursor.execute("DELETE FROM Customer WHERE CustomerID = %s", (CustomerID,))
            # Commit the transaction to save changes to the database
            conn.commit()
            print("Customer deleted successfully.")
    except Exception as e:
        # Catch and display any errors that occur during the deletion
        print(f"Error deleting customer: {e}")

def search_customer(conn, CustomerID):
    """
    Searches for a customer in the database by CustomerID.
    
    Args:
        conn: Database connection object
        CustomerID: Unique identifier for the customer to find
        
    Returns:
        tuple: Customer data if found
        None: If no customer with the given ID exists
        
    The function also prints the customer information if found.
    """
    try:
        # Use a cursor to execute the SQL SELECT statement
        with conn.cursor() as cursor:
            # Prepare SQL statement with placeholder for CustomerID
            cursor.execute("SELECT * FROM Customer WHERE CustomerID = %s", (CustomerID,))
            # Fetch the first matching row (should be only one since CustomerID is primary key)
            customer = cursor.fetchone()
            
            # Check if a customer was found and handle accordingly
            if customer:
                print(customer)  # Display customer information
                return customer  # Return the customer data
            else:
                print("Customer not found.")
                return None
    except Exception as e:
        # Catch and display any errors that occur during the search
        print(f"Error searching for customer: {e}")
        return None

def create_customer(conn, CustomerID, first_name, last_name, email, phonenumber, homeaddress, isActive, signupdate, rewardspoints):
    """
    Creates a new customer record in the database.
    
    Args:
        conn: Database connection object
        CustomerID: Unique identifier for the new customer
        first_name: Customer's first name
        last_name: Customer's last name
        email: Customer's email address
        phonenumber: Customer's phone number
        homeaddress: Customer's home address
        isActive: Boolean indicating if the customer account is active
        signupdate: Date when the customer signed up (YYYY-MM-DD format)
        rewardspoints: Integer representing customer's initial reward points
        
    Returns:
        None: Displays success or error message
    """
    try:
        # Use a cursor to execute the SQL INSERT statement
        with conn.cursor() as cursor:
            # Prepare SQL statement with placeholders for safe parameter insertion
            cursor.execute("INSERT INTO Customer (CustomerID, FirstName, LastName, Email, PhoneNumber, HomeAddress, IsActive, SignUpdate, RewardPoints) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                           , (CustomerID, first_name, last_name, email, phonenumber, homeaddress, isActive, signupdate, rewardspoints))
            # Commit the transaction to save changes to the database
            conn.commit()
            print("Customer created successfully.")
    except Exception as e:
        # Catch and display any errors that occur during creation
        # Common errors might include duplicate CustomerID or constraint violations
        print(f"Error creating customer: {e}")