

"""
staff.py - Module for Staff Management in MuskieCo Store Management System

This module provides functionality for managing staff records across different stores.
It includes operations for adding, updating, deleting, and searching staff records
in the database.

Each staff member is uniquely identified by a StaffID and is associated with a specific
store via the StoreID. Staff records include personal information such as name, age,
contact details, and employment information.
"""

def staff(conn):
    """
    Main staff management function providing a menu-driven interface for staff operations.
    
    This function displays a menu with options to add, update, delete, or search for staff
    records. Based on user selection, it collects the necessary information and calls the
    appropriate function to perform the requested operation.
    
    Parameters:
        conn: Database connection object used to interact with the database
              Must be an active connection with appropriate access privileges
    
    Menu Options:
        1. Add Staff - Create a new staff record with all required information
        2. Update Staff - Modify an existing staff record's fields
        3. Delete Staff - Remove a staff record from the database
        4. Search Staff - Look up and display a staff member's information
    
    Returns:
        None
    """
    print("1. Add Staff")
    print("2. Update Staff")
    print("3. Delete Staff")
    print("4. Search Staff")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            StaffID = int(input("Enter Staff ID: "))
            StoreId = int(input("Enter Store ID: "))
            Name = input("Enter Name: ")
            Age = int(input("Enter Age: "))
            HomeAddress = input("Enter home address: ")
            PhoneNumber = input("Enter phone number: ")
            Email = input("Enter email: ")
            StartDate = input("Enter start date (YYYY-MM-DD): ")
            create_staff(conn,StaffID, StoreId, Name, Age, HomeAddress, PhoneNumber, Email, StartDate)
        case 2:
            staff_data = search_staff(conn,input("Enter Staff ID: "))
            if not staff_data:
                print("No staff found")
                return
            staff = list(staff_data)
            print("What would you like to update?")
            print("1. Store ID")
            print("2. Name")
            print("3. Age")
            print("4. Home Address")
            print("5. Phone Number")
            print("6. Email")
            print("7. Start Date")
            choice = int(input("Enter choice: "))
            match choice:
                case 1:
                    staff[1] = int(input("Enter new Store ID: "))
                case 2:
                    staff[2] = input("Enter new Name: ")
                case 3:
                    staff[3] = int(input("Enter new Age: "))
                case 4:
                    staff[4] = input("Enter new Home Address: ")
                case 5:
                    staff[5] = input("Enter new Phone Number: ")
                case 6:
                    staff[6] = input("Enter new Email: ")
                case 7:
                    staff[7] = input("Enter new Start Date: ")
            update_staff(conn, staff[0],staff[1],staff[2],staff[3],staff[4],staff[5],staff[6],staff[7])
        case 3:
            delete_staff(conn,input("Enter Staff ID: "))
        case 4:
            search_staff(conn,input("Enter Staff ID: "))

def update_staff(conn, StaffID, StoreId, Name, Age, HomeAddress, PhoneNumber, Email, StartDate):
    """
    Update an existing staff record in the database.
    
    This function modifies a staff record identified by StaffID, updating all fields
    with the provided values. The function executes an SQL UPDATE statement to modify
    the staff record in the database.
    
    Parameters:
        conn: Database connection object
        StaffID: Unique identifier of the staff member to be updated
        StoreId: ID of the store where the staff member works
        Name: Full name of the staff member
        Age: Age of the staff member (integer)
        HomeAddress: Home address of the staff member
        PhoneNumber: Contact phone number of the staff member
        Email: Email address of the staff member
        StartDate: Employment start date in YYYY-MM-DD format
    
    Returns:
        None
    
    Raises:
        Exception: Prints error message if update operation fails
    """
    try:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE Staff SET StoreId = %s, Name = %s, Age = %s, HomeAddress = %s, PhoneNumber = %s, Email = %s, StartDate = %s WHERE StaffID = %s",
                           (StoreId, Name, Age, HomeAddress, PhoneNumber, Email, StartDate, StaffID))
            conn.commit()
            print("Staff updated successfully.")
    except Exception as e:
        print(f"Error updating staff: {e}")

def delete_staff(conn,StaffID):
    """
    Delete a staff record from the database.
    
    This function removes a staff record identified by StaffID from the database.
    The function executes an SQL DELETE statement to remove the staff record.
    
    Parameters:
        conn: Database connection object
        StaffID: Unique identifier of the staff member to be deleted
    
    Returns:
        None
    
    Raises:
        Exception: Prints error message if deletion operation fails
    """
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM Staff WHERE StaffID = %s", (StaffID,))
            conn.commit()
            print("Staff deleted successfully.")
    except Exception as e:
        print(f"Error deleting staff: {e}")

def search_staff(conn, StaffID):
    """
    Search for and retrieve a staff record from the database.
    
    This function looks up a staff record identified by StaffID and returns
    the complete record if found. The function executes an SQL SELECT statement
    to retrieve the staff record from the database.
    
    Parameters:
        conn: Database connection object
        StaffID: Unique identifier of the staff member to search for
    
    Returns:
        tuple: The staff record as a tuple containing all fields if found
        None: If no matching staff record is found or an error occurs
    
    Raises:
        Exception: Prints error message if search operation fails
    """
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Staff WHERE StaffID = %s", (StaffID,))
            staff = cursor.fetchone()
            if staff:
                print(staff)
                return staff
            else:
                print("Staff not found.")
                return None
    except Exception as e:
        print(f"Error searching for staff: {e}")
        return None

def create_staff(conn, StaffID, StoreId, Name, Age, HomeAddress, PhoneNumber, Email, StartDate):
    """
    Add a new staff record to the database.
    
    This function creates a new staff record with the specified information.
    The function executes an SQL INSERT statement to add the new staff record
    to the database.
    
    Parameters:
        conn: Database connection object
        StaffID: Unique identifier for the new staff member
        StoreId: ID of the store where the staff member works
        Name: Full name of the staff member
        Age: Age of the staff member (integer)
        HomeAddress: Home address of the staff member
        PhoneNumber: Contact phone number of the staff member
        Email: Email address of the staff member
        StartDate: Employment start date in YYYY-MM-DD format
    
    Returns:
        None
    
    Raises:
        Exception: Prints error message if insertion operation fails
                  Common failures include duplicate StaffID or referential
                  integrity violations if StoreId doesn't exist
    """
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO Staff (StaffID, StoreId, Name, Age, HomeAddress, PhoneNumber, Email, StartDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                           (StaffID, StoreId, Name, Age, HomeAddress, PhoneNumber, Email, StartDate))
            conn.commit()
            print("Staff created successfully.")
    except Exception as e:
        print(f"Error creating staff: {e}")