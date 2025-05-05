
"""
rewards.py - Module for Customer and Employee Rewards Management

This module provides functionality for managing the rewards system in the MuskieCo Store 
Management System. It includes functions to retrieve reward points for customers and 
calculate employee rewards based on customer sign-ups.

The rewards system tracks customer loyalty through accumulated reward points and
recognizes employee performance by counting the number of customers they've signed up.
"""

def customer_rewards(conn):
    """
    Retrieves reward points for a specified customer from the database.
    
    This function prompts the user to enter a customer ID, then queries the database
    to retrieve the reward points associated with that customer. The results are 
    displayed to the user and returned to the calling function.
    
    Parameters:
        conn: Database connection object used to interact with the database
              Must be an active connection with appropriate access privileges
    
    Returns:
        tuple: A tuple containing the customer's reward points if the customer is found
        None: If no customer with the given ID exists or if an error occurs
    
    Raises:
        Exception: Catches and prints any database errors that occur during execution
    """
    customer_id = input("Enter customer id: ")
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT RewardPoints FROM Customer WHERE CustomerID = %s", (customer_id,))
            customer = cursor.fetchone()
            if customer:
                print(customer)
                return customer
            else:
                print("Customer not found.")
                return None
    except Exception as e:
        print(f"Error searching for customer: {e}")
        return None

def employee_rewards(conn):
    """
    Calculates rewards for an employee based on customer sign-ups.
    
    This function prompts the user to enter an employee ID and a month, then queries
    the database to count how many customers the specified employee has signed up.
    The results are displayed to the user as part of an employee rewards program.
    
    Parameters:
        conn: Database connection object used to interact with the database
              Must be an active connection with appropriate access privileges
    
    Returns:
        None: This function always returns None after displaying the results
    
    Raises:
        Exception: Catches and prints any database errors that occur during execution
    
    Note:
        Although the function requests a month input, the current implementation 
        does not filter by month in the SQL query. The month parameter could be 
        used in future enhancements to filter sign-ups by specific time periods.
    """
    employee_id = input("Enter employee id: ")
    month = input("Enter month: ")
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT Count(CustomerID) FROM CustomerSignUp WHERE SignUpStaffID = %s", employee_id)
            rewards = cursor.fetchall()
            print(rewards)
            return None
    except Exception as e:
        print(f"Error searching for employee: {e}")
        return None