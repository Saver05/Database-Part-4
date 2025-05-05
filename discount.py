
"""
discount.py - Module for Discount Management in MuskieCo Store Management System

This module provides functionality for managing product discounts across different stores.
It includes operations for adding, updating, deleting, and viewing discount records
in the database.

Each discount is uniquely identified by a DiscountID and associates a ProductID with
a StoreID, indicating that the specified product has a discount at the specified store.
"""

def discount(conn):
    """
    Main discount management function providing a menu-driven interface for discount operations.
    
    This function displays a menu with options to add, update, delete, or view discount records.
    Based on user selection, it calls the appropriate function to perform the requested operation.
    
    Parameters:
        conn: Database connection object used to interact with the database
              Must be an active connection with appropriate access privileges
    
    Menu Options:
        1. Add Discount - Create a new discount record
        2. Update Discount - Modify an existing discount record
        3. Delete Discount - Remove a discount record
        4. View Discount - Display information about a specific discount
    
    Returns:
        None
    """
    print("1. Add Discount")
    print("2. Update Discount")
    print("3. Delete Discount")
    print("4. View Discount")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            discount_id = int(input("Enter Discount ID: "))
            product_id = int(input("Enter Product ID: "))
            store_id = int(input("Enter Store ID: "))
            add_discount(conn, discount_id, product_id, store_id)
        case 2:
            discount_id = int(input("Enter Discount ID: "))
            discount_data = search_discount(conn, discount_id)
            discount = list(discount_data)
            print("What would you like to update?")
            print("1. Product ID")
            print("2. Store ID")
            match int(input("Enter choice: ")):
                case 1:
                    discount[1] = int(input("Enter new Product ID: "))
                case 2:
                    discount[2] = int(input("Enter new Store ID: "))
            update_discount(conn, discount_id, discount[1], discount[2])
        case 3:
            delete_discount(conn, input("Enter Discount ID: "))
        case 4:
            discount_id = int(input("Enter Discount ID: "))
            search_discount(conn, discount_id)
        case _:
            print("Invalid choice. Please try again.")


def delete_discount(conn, discount_id):
    """
    Delete a discount record from the database.
    
    This function removes a discount record identified by its discount_id from the database.
    
    Parameters:
        conn: Database connection object
        discount_id: Unique identifier of the discount record to be deleted
    
    Returns:
        None
    
    Raises:
        Exception: Prints error message if deletion operation fails
    """
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM Discount WHERE DiscountID = %s", (discount_id,))
            conn.commit()
            print("Discount deleted successfully.")
    except Exception as e:
        print(f"Error deleting discount: {e}")

def update_discount(conn, discount_id, product_id, store_id):
    """
    Update an existing discount record in the database.
    
    This function modifies a discount record identified by its discount_id, updating
    the associated product_id and store_id values.
    
    Parameters:
        conn: Database connection object
        discount_id: Unique identifier of the discount record to be updated
        product_id: New product ID to associate with this discount
        store_id: New store ID to associate with this discount
    
    Returns:
        None
    
    Raises:
        Exception: Prints error message if update operation fails
    """
    try:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE Discount SET ProductID = %s, StoreID = %s WHERE DiscountID = %s",
                           (product_id, store_id, discount_id))
            conn.commit()
            print("Discount updated successfully.")
    except Exception as e:
        print(f"Error updating discount: {e}")

def search_discount(conn, discount_id):
    """
    Search for and retrieve a discount record from the database.
    
    This function looks up a discount record identified by its discount_id and
    returns the complete record if found.
    
    Parameters:
        conn: Database connection object
        discount_id: Unique identifier of the discount record to search for
    
    Returns:
        tuple: The discount record as a tuple containing all fields if found
        None: If no matching discount record is found or an error occurs
    
    Raises:
        Exception: Prints error message if search operation fails
    """
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Discount WHERE DiscountID = %s", (discount_id,))
            discount = cursor.fetchone()
            if discount:
                print(discount)
                return discount
            else:
                print("Discount not found.")
                return None
    except Exception as e:
        print(f"Error searching for discount: {e}")
        return None

def add_discount(conn, discount_id, product_id, store_id):
    """
    Add a new discount record to the database.
    
    This function creates a new discount record with the specified discount_id,
    product_id, and store_id values.
    
    Parameters:
        conn: Database connection object
        discount_id: Unique identifier for the new discount record
        product_id: ID of the product to which the discount applies
        store_id: ID of the store where the discount is offered
    
    Returns:
        None
    
    Raises:
        Exception: Prints error message if insertion operation fails
                  Common failures include duplicate discount_id or referential
                  integrity violations if product_id or store_id don't exist
    """
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO Discount (DiscountID, ProductID, StoreID) VALUES (%s, %s, %s)",
                           (discount_id, product_id, store_id))
            conn.commit()
            print("Discount added successfully.")
    except Exception as e:
        print(f"Error adding discount: {e}")