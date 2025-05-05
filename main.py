# main.py - Main entry point for the MuskieCo management system
# This file implements a menu-driven interface for store, inventory, and transaction management
import staff
import store
from discount import discount as discountFn
from customer import customer as customerFn
from database import *  # Import all database functions from database.py


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
            # Display the product management submenu
            print("\n--- Inventory Records ---")
            print("1. Add Product")
            print("2. Update Product")
            print("3. Delete Product")
            sub_choice = input("Enter choice: ")

            # Using Python 3.10's match-case statement for cleaner code structure
            # This is more readable than nested if-elif-else statements for many options
            match sub_choice:
                # Option 1: Add a new product
                # Collects product information and adds it to the database
                case 1:
                    # Collect all required information for a new product through user input
                    product_id = get_input("Enter Product ID: ")
                    product_name = get_input("Enter Product Name: ")
                    QuantityInStock = int(get_input("Enter Quantity In Stock: "))
                    BuyPrice = float(get_input("Enter Buy Price: "))
                    SellPrice = float(get_input("Enter Sell Price: "))
                    store_id = int(get_input("Enter Store ID: "))
                    
                    # Add the product to the database using the collected information
                    # The add_product function is defined in database.py
                    add_product(conn, product_id, product_name, QuantityInStock, BuyPrice, SellPrice, store_id)

                # Option 2: Update an existing product
                # Allows modifying product details like name, quantity, prices, and store
                case 2:
                    product_id = get_input("Enter Product ID: ")  # Get ID of product to update
                    
                    # Retrieve product details to display and update
                    # get_product fetches the product record and returns it as a tuple
                    product = get_product(conn, product_id)
                    
                    # Only proceed with the update if the product was found in the database
                    if product:
                        # Show update options submenu
                        print("\n--- What would you like to update? ---")
                        print("1. Product Name")
                        print("2. Quantity In Stock")
                        print("3. Buy Price")
                        print("4. Sell Price")
                        print("5. Store ID")
                        update_choice = input("Enter choice: ")

                        # Using another match-case for update options
                        # This creates a nested menu structure for product updates
                        match update_choice:
                            # Update product name
                            case 1:
                                product_name = get_input("Enter new Product Name: ")
                                # Access product tuple elements by index:
                                # product[0] = ProductID, product[1] = ProductName, product[2] = QuantityInStock,
                                # product[3] = BuyPrice, product[4] = SellPrice, product[5] = StoreID
                                # Keep other fields the same, only update the name
                                update_product(conn, product[0], product_name, product[2], product[3], product[4],
                                               product[5])

                            # Update quantity in stock
                            case 2:
                                QuantityInStock = float(get_input("Enter new Quantity In Stock: "))
                                # Keep other fields the same, only update the quantity
                                update_product(conn, product[0], product[1], product[2], QuantityInStock, product[4],
                                               product[5])

                            # Update buy price
                            case 3:
                                BuyPrice = float(get_input("Enter new Buy Price: "))
                                # Keep other fields the same, only update the buy price
                                update_product(conn, product[0], product[1], product[2], BuyPrice, product[4],
                                               product[5])

                            # Update sell price
                            case 4:
                                SellPrice = float(get_input("Enter new Sell Price: "))
                                # Keep other fields the same, only update the sell price
                                update_product(conn, product[0], product[1], product[2], product[3], SellPrice,
                                               product[5])

                            # Update store ID
                            case 5:
                                store_id = int(get_input("Enter new Store ID: "))
                                # Keep other fields the same, only update the store ID
                                update_product(conn, product[0], product[1], product[2], product[3], product[4],
                                               store_id)

                            # Handle invalid update choice with wildcard pattern match
                            case _:
                                print("Invalid choice. Please try again.")

                # Option 3: Delete a product
                # Removes a product from the database by ID after confirmation
                case 3:
                    product_id = get_input("Enter Product ID: ")  # Get ID of product to delete
                    
                    # Display product information before deletion for verification
                    # get_product retrieves and displays the product details
                    get_product(conn, product_id)
                    
                    # Ask for confirmation before deleting the product
                    print("\n--- Are you sure you want to delete this product? ---")
                    update_choice = input("Enter 'yes' to confirm: ")
                    
                    # Handle the deletion confirmation options
                    match update_choice:
                        case "yes":
                            # Delete the product if user confirmed
                            delete_product(conn, product_id)
                            print("Product deleted successfully.")
                        case "no":
                            # Cancel deletion if user chose not to proceed
                            print("Product deletion cancelled.")
                        case _:
                            # Handle any input other than 'yes' or 'no'
                            print("Invalid choice. Please try again.")

                # Handle invalid product menu choice with wildcard pattern match
                case _:
                    print("Invalid choice. Please try again.")

            # Note: This section is marked as a placeholder for additional inventory functions
            # Future implementations could include stock adjustments, transfers, etc.

        # =====================================================================
        # Billing and Transaction Records menu
        # Handles transactions including adding new transactions,
        # adding products to transactions, and calculating totals
        # =====================================================================
        elif choice == "3":
            # Display the transaction management submenu
            print("\n--- Billing and Transaction Records ---")
            print("1. Add Transaction")
            print("2. Add Product to Transaction")
            print("3. Calculate Transaction Total")
            sub_choice = input("Enter choice: ")
            
            # Using match-case to handle transaction menu options
            match sub_choice:
                # Option 1: Add a new transaction
                # Creates a new transaction record with customer, store, and cashier info
                case 1:
                    # Collect all required information for a new transaction
                    storeid = int(input("Enter Store ID: "))        # Store where transaction occurred
                    customerid = int(input("Enter Customer ID: "))  # Customer who made the purchase
                    cashierid = int(input("Enter Cashier ID: "))    # Staff who processed the transaction
                    purchasedate = input("Enter Purchase Date: ")  # Date of purchase
                    totalprice = float(input("Total Price: "))        # Initial total price
                    Transactiontype = input("Transaction Type: ")  # Buy or Return
                    
                    # Add the transaction to the database and display the generated ID
                    print("Transaction id: "+ str(add_transaction(conn, storeid, customerid, cashierid, purchasedate, totalprice, Transactiontype)))
                
                # Option 2: Add a product to an existing transaction
                # Associates products with transactions and records quantities
                case 2:
                    transaction_id = int(input("Enter Transaction ID: "))

                    # Collect multiple products to add to the transaction
                    # Using a loop to allow adding any number of products
                    product_entries = []
                    while True:
                        # Get product ID or exit the loop if user is done
                        product_id = input("Enter Product ID (or 'done' to finish): ")
                        if product_id.lower() == "done":
                            break
                        
                        # Get quantity of this product in the transaction
                        quantity = input("Enter Quantity: ")
                        
                        # Get discount percentage applied to this product
                        # Discounts are stored as percentages (e.g., 10 for 10%)
                        discount = input("Discount Applied %: ")
                    
                        # Add the product data to our collection
                        # Using dictionary to organize the data for each product
                        product_entries.append({
                            'product_id': product_id,    # The product identifier
                            'quantity': quantity,        # How many units were purchased
                            'discount': discount         # Discount percentage applied
                        })
                    
                    # Add all products to the transaction in a single database operation
                    # This ensures all products are added or none are (transaction integrity)
                    # The function handles the SQL insert operations for all products
                    add_products_to_transaction(conn, transaction_id, product_entries)
                                    
                                    # Option 3: Calculate the total price of a transaction
                                    # Computes the sum of all products in a transaction
                                    # Total is based on sell price, quantity, and any discounts
                case 3:
                    # Get the transaction ID to calculate
                    # The ID identifies which transaction to compute total for
                    transactionid = int(input("Enter Transaction ID: "))
                    
                    # Display the current transaction details for reference
                    # This shows what items are included in the total
                    get_transaction(conn, transactionid)
                    
                    # Calculate and display the total price of all items in the transaction
                    # This function computes the sum based on product prices and quantities
                    totalprice = get_transaction_price(conn, transactionid)
                    print("Transaction Total: "+str(totalprice))
                                    
                                    # Handle invalid transaction menu choice with wildcard pattern match
                                    # Provides feedback if user enters an unrecognized option
                case _:
                    print("Invalid choice. Please try again.")
                    
                            # =====================================================================
                            # Reports menu
                            # Handles generation of various business reports
                            # These reports provide business insights and statistics
                            # =====================================================================
        elif choice == "4":
            # Display the reports menu
            # Each option generates a different type of business report
            print("\n--- Reports ---")
            print("1. Monthly Customer Activity Report")
            print("2. Annual Sales Report")
            print("3. Product Stock Report")
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
                    month = int(input("Enter Month (YYYY-MM): "))
                    
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
                    sales = get_sales_report(conn, store_id, year)
                                    
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
                                    
                                    # Handle invalid report menu choice with wildcard pattern match
                                    # Provides feedback if user enters an unrecognized option
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
                    
        # Close the database connection when exiting the program
        # This ensures proper cleanup of database resources
        # Prevents database connection leaks and resource issues
        conn.close()
                    
# Standard Python idiom to ensure main() is only called when the script is run directly
# This allows the script to be imported without running the main function
# Useful for testing or when incorporating this code into larger systems
if __name__ == "__main__":
    main()
