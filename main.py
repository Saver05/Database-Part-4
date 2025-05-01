# main.py - Main entry point for the MuskieCo management system
# This file implements a menu-driven interface for store, inventory, and transaction management
from database import *  # Import all database functions from database.py


def main():
    """
    Main function that serves as the entry point for the MuskieCo management system.
    
    This function creates a database connection and presents a menu-driven interface
    allowing users to perform various operations including:
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
            # Display the store management submenu
            print("\n--- Information Processing ---")
            print("1. Add Store")
            print("2. Update Store")
            print("3. Delete Store")
            print("4. Search Store")
            sub_choice = input("Enter choice: ")

            # Option 1: Add a new store
            # Collects store information and adds it to the database
            if sub_choice == "1":
                # Collect all required information for a new store through user input
                store_address = get_input("Store Address")  # Get the store address from user
                phone_number = get_input("Phone Number")    # Get the phone number from user
                manager_id = get_input("Manager ID")        # Get the manager ID from user
                
                # Add the store to the database using the collected information
                # The add_store function is defined in database.py
                add_store(conn, store_address, phone_number, manager_id)

            # Option 2: Update an existing store
            # Allows modifying store details like address, phone number, and manager
            elif sub_choice == "2":
                print("Enter the store ID to update.")
                store_id = get_input("Store ID")  # Get ID of store to update
                
                # Retrieve store details to display and update
                # search_store fetches the store record and returns it as a tuple
                store = search_store(conn, store_id)
                
                # Only proceed with the update if the store was found in the database
                if store:
                    # Show update options submenu
                    print("What would you like to update?")
                    print("1. Store Address")
                    print("2. Phone Number")
                    print("3. Manager ID")
                    sub_choice = input("Enter choice: ")

                    # Update store address
                    if sub_choice == "1":
                        new_address = get_input("New Store Address")
                        # Access store tuple elements by index:
                        # store[0] = StoreID, store[1] = ManagerID, store[2] = StoreAddress, store[3] = PhoneNumber
                        # Keep other fields the same, only update the address
                        update_store(conn, store[0], new_address, store[3], store[1])

                    # Update phone number
                    elif sub_choice == "2":
                        new_phone_number = get_input("New Phone Number")
                        # Keep other fields the same, only update the phone number
                        update_store(conn, store[0], store[2], new_phone_number, store[1])

                    # Update manager ID
                    elif sub_choice == "3":
                        new_manager_id = get_input("New Manager ID")
                        # Keep other fields the same, only update the manager ID
                        update_store(conn, store[0], store[2], store[3], new_manager_id)

                    # Handle invalid update choice
                    else:
                        print("Invalid choice. Please try again.")

            # Option 3: Delete a store
            # Removes a store from the database by ID
            elif sub_choice == "3":
                store_id = get_input("Store ID")  # Get ID of store to delete
                # Delete the store with the given ID from the database
                delete_store(conn, store_id)

            # Option 4: Search for a store
            # Retrieves and displays store information by ID
            elif sub_choice == "4":
                store_id = get_input("Store ID")  # Get ID of store to search for
                # Search for and display store information
                # search_store handles both retrieval and display of the store data
                search_store(conn, store_id)

            # Handle invalid store menu choice
            else:
                print("Invalid option please try again.")

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
                    QuantityInStock = get_input("Enter Quantity In Stock: ")
                    BuyPrice = get_input("Enter Buy Price: ")
                    SellPrice = get_input("Enter Sell Price: ")
                    store_id = get_input("Enter Store ID: ")
                    
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
                                QuantityInStock = get_input("Enter new Quantity In Stock: ")
                                # Keep other fields the same, only update the quantity
                                update_product(conn, product[0], product[1], product[2], QuantityInStock, product[4],
                                               product[5])

                            # Update buy price
                            case 3:
                                BuyPrice = get_input("Enter new Buy Price: ")
                                # Keep other fields the same, only update the buy price
                                update_product(conn, product[0], product[1], product[2], BuyPrice, product[4],
                                               product[5])

                            # Update sell price
                            case 4:
                                SellPrice = get_input("Enter new Sell Price: ")
                                # Keep other fields the same, only update the sell price
                                update_product(conn, product[0], product[1], product[2], product[3], SellPrice,
                                               product[5])

                            # Update store ID
                            case 5:
                                store_id = get_input("Enter new Store ID: ")
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
                    storeid = input("Enter Store ID: ")        # Store where transaction occurred
                    customerid = input("Enter Customer ID: ")  # Customer who made the purchase
                    cashierid = input("Enter Cashier ID: ")    # Staff who processed the transaction
                    purchasedate = input("Enter Purchase Date: ")  # Date of purchase
                    totalprice = input("Total Price: ")        # Initial total price
                    Transactiontype = input("Transaction Type: ")  # Buy or Return
                    
                    # Add the transaction to the database and display the generated ID
                    print("Transaction id: "+add_transaction(conn, storeid, customerid, cashierid, purchasedate, totalprice, Transactiontype))
                
                # Option 2: Add a product to an existing transaction
                # Associates products with transactions and records quantities
                case 2:
                    # Get the transaction ID to which the product will be added
                    transactionid = input("Enter Transaction ID: ")
                    
                    # Display the current transaction details for reference
                    get_transaction(conn, transactionid)
                    
                    # Collect product information to add to the transaction
                    productid = input("Enter Product ID: ")       # Product being purchased
                    quantity = input("Enter Quantity: ")          # Number of items purchased
                    discountapplied = input("Discount Applied %: ")  # Discount percentage if any
                    
                    # Add the product to the transaction in the database
                    add_product_transaction(conn, transactionid, productid, quantity, discountapplied)
                
                # Option 3: Calculate the total price of a transaction
                # Computes the sum of all products in a transaction
                case 3:
                    # Get the transaction ID to calculate
                    transactionid = input("Enter Transaction ID: ")
                    
                    # Display the current transaction details for reference
                    get_transaction(conn, transactionid)
                    
                    # Calculate and display the total price of all items in the transaction
                    totalprice = get_transaction_price(conn, transactionid)
                    print("Transaction Total: "+str(totalprice))
                
                # Handle invalid transaction menu choice with wildcard pattern match
                case _:
                    print("Invalid choice. Please try again.")

        # =====================================================================
        # Reports menu (placeholder for future functionality)
        # Will handle generation of various business reports
        # =====================================================================
        elif choice == "4":
            # Display the reports menu
            print("\n--- Reports ---")
            print("1. Monthly Customer Activity Report")
            print("2. Annual Sales Report")
            print("3. Product Stock Report")
            sub_choice = input("Enter choice: ")
            
            # This section is a placeholder for future reporting functionality
            # Would implement generation of various business reports such as:
            # - Customer activity tracking
            # - Sales analysis over time
            # - Inventory levels and turnover rates
            print("This functionality is not yet implemented.")

        # =====================================================================
        # Exit the program
        # Breaks out of the main loop and closes the database connection
        # =====================================================================
        elif choice == "0":
            print("Exiting...")
            break  # Exit the main program loop

        # =====================================================================
        # Handle invalid main menu choice
        # Catches any input that doesn't match valid menu options
        # =====================================================================
        else:
            print("Invalid choice. Please try again.")

    # Close the database connection when exiting the program
    # This ensures proper cleanup of database resources
    conn.close()

# Standard Python idiom to ensure main() is only called when the script is run directly
# This allows the script to be imported without running the main function
if __name__ == "__main__":
    main()
