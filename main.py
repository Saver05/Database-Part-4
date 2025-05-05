# main.py - Main entry point for the MuskieCo management system
# This file implements a menu-driven interface for store, inventory, and transaction management
import products
import staff
import store
from discount import discount as discountFn
from customer import customer as customerFn
from database import *  # Import all database functions from database.py
from transactions import transactions as transaction
from rewards import customer_rewards, employee_rewards

def main():
    """
    Main function that serves as the entry point for the MuskieCo management system.
    
    This function creates a database connection and presents a menu-driven interface
    allowing users to perform various operations including
    - Information Processing (store management)
    - Inventory Records (product management)
    - Billing and Transaction Records
    - Reports generation
    
    The function handles user input and calls appropriate database functions
    based on user selections.
    """
    # Establish database connection at program start
    # This connection will be used throughout the program for all database operations
    conn = connect_to_database()
    
    # Main program loop - continues until the user chooses to exit
    while True:
        # Display main menu options to the user
        # The menu provides access to the main modules of the system
        print("--- MuskieCo Main Menu ---")
        print("Which task would you like to perform?")
        print("1. Information Processing")  # Store management
        print("2. Inventory Records")       # Product management
        print("3. Billing and Transaction Records")
        print("4. Reports")
        print("0. Exit")  # Option to exit the program
        choice = input("Enter the number corresponding to your choice: ")  # Get user's menu selection

        # =====================================================================
        # Information Processing menu (Store management)
        # Handles store operations including add, update, delete, and search
        # =====================================================================
        if choice == "1":
            print("1. Stores")
            print("2. Customers")
            print("3. Staff")
            print("4. Discount")
            choice = input("Enter the number corresponding to your choice: ")
            match choice:
                case "1":
                    store.store(conn)
                case "2":
                    customerFn(conn)
                case "3":
                    staff.staff(conn)
                case "4":
                    discountFn(conn)
                case _:
                    print("Invalid choice. Please try again.")
        # =====================================================================
        # Inventory Records menu (Product management)
        # Handles product operations including add, update, and delete
        # =====================================================================
        elif choice == "2":
            products.products(conn)
        # =====================================================================
        # Billing and Transaction Records menu
        # Handles transactions including adding new transactions,
        # adding products to transactions, and calculating totals
        # =====================================================================
        elif choice == "3":
            # Display the transaction management submenu
            print("\n--- Billing and Transaction Records ---")
            print("1. Manage Transactions")
            print("2. Generate reward notices for members")
            print("3. Generate rewards checks for employees")
            choice = int(input("Enter choice: "))
            match choice:
                case 1:
                    transaction(conn)
                case 2:
                    customer_rewards(conn)
                case 3:
                    employee_rewards(conn)
        elif choice == "4":
            # Display the reports menu
            # Each option generates a different type of business report
            print("\n--- Reports ---")
            print("1. Monthly Customer Activity Report")
            print("2. Annual Sales Report")
            print("3. Product Stock Report")
            print("4. Daily Sales Report")
            print("5. Monthly Sales Report")
            print("6. Store Stock Report")
            sub_choice = input("Enter choice: ")

            # Using match-case to handle reports menu options
            # Each case handles generating a different report
            match sub_choice:
                # Option 1: Generate monthly customer activity report
                # Shows all transactions for a specific customer in a given month
                case "1":
                    # Get the customer ID for the report
                    customerid = int(input("Enter Customer ID: "))
                    
                    # Retrieve and display customer information for verification
                    # This confirms we have the right customer
                    customer = get_customer(conn, customerid)
                    
                    # Get the month in YYYY-MM format to filter transactions
                    month = int(input("Enter Month (MM): "))
                    
                    # Generate and display the report of transactions for this customer and month
                    # The function handles retrieving and formatting the transaction data
                    transactions = get_transactions_month(conn, customerid, month)
                                    
                # Option 2: Generate annual sales report
                # Shows all sales for a specific store in a given year
                case "2":
                    # Get the store ID for the report
                    store_id = int(input("Enter Store ID: "))
                    
                    # Retrieve and display store information for verification
                    # This confirms we have the right store
                    search_store(conn, store_id)
                    
                    # Get the year to filter transactions
                    year = int(input("Enter year (YYYY):"))
                    
                    # Generate and display the annual sales report for this store and year
                    # The function handles retrieving and formatting the sales data
                    sales = get_sales_report_year(conn, store_id, year)
                                    
                # Option 3: Generate product stock report
                # Shows current inventory levels for specified products at a store
                case "3":
                    # Get the store ID for the report
                    store_id = int(input("Enter Store ID: "))
                    
                    # Retrieve and display store information for verification
                    # This confirms we have the right store
                    search_store(conn, store_id)
                    
                    # Collect multiple product IDs to include in the report
                    # Using a loop to allow adding any number of products
                    product_ids = []
                    while True:
                        # Get product ID or exit the loop if user is done
                        product_id = input("Enter Product ID (or 'done' to finish): ")
                        if product_id.lower() == "done":
                            break
                        # Add this product ID to our collection
                        product_ids.append(product_id)
                    
                    # Generate and display the stock report for these products at this store
                    # The function handles retrieving and formatting the inventory data
                    get_products_quantity(conn, store_id, product_ids)
                case "4":
                    store_id = int(input("Enter Store ID: "))
                    search_store(conn, store_id)
                    get_day_sales_report(conn,store_id,input("Enter day (YYYY-MM-DD): "))
                case "5":
                    store_id = int(input("Enter Store ID: "))
                    search_store(conn, store_id)
                    get_monthly_sales_report(conn,store_id,input("Enter year (YYYY)"), input("Enter month (MM): "))
                case "6":
                    store_id = int(input("Enter Store ID: "))
                    get_all_products_quantity(conn, store_id)
                case _:
                    print("Invalid choice. Please try again.")
                    
        # =====================================================================
        # Exit the program
        # Breaks out of the main loop and closes the database connection
        # This is the clean way to terminate the program
        # =====================================================================
        elif choice == "0":
            print("Exiting...")
            break  # Exit the main program loop
                    
        # =====================================================================
        # Handle invalid main menu choice
        # Catches any input that doesn't match valid menu options
        # Provides feedback if user enters an unrecognized option
        # =====================================================================
        else:
            print("Invalid choice. Please try again.")
                    
# Standard Python idiom to ensure main() is only called when the script is run directly
# This allows the script to be imported without running the main function
# Useful for testing or when incorporating this code into larger systems
if __name__ == "__main__":
    main()
