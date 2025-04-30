# main.py - Main entry point for the MuskieCo management system
from database import add_store, update_store, delete_store, search_store, get_input, connect_to_database, add_product, \
    get_product, update_product, delete_product


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
    conn = connect_to_database()
    # Main program loop
    while True:
        # Display main menu options
        print("--- MuskieCo Main Menu ---")
        print("Which task would you like to perform?")
        print("1. Information Processing")
        print("2. Inventory Records")
        print("3. Billing and Transaction Records")
        print("4. Reports")
        print("0. Exit")
        choice = input("Enter the number corresponding to your choice: ")

        # Information Processing menu (Store management)
        if choice == "1":
            print("\n--- Information Processing ---")
            print("1. Add Store")
            print("2. Update Store")
            print("3. Delete Store")
            print("4. Search Store")
            sub_choice = input("Enter choice: ")

            # Option 1: Add a new store
            if sub_choice == "1":
                # Collect all required information for a new store
                store_address = get_input("Store Address")  # Get the store address from user input
                phone_number = get_input("Phone Number")
                manager_id = get_input("Manager ID")
                # Add the store to the database
                add_store(conn, store_address, phone_number, manager_id)  # Call the add_store function

            # Option 2: Update an existing store
            elif sub_choice == "2":
                print("Enter the store ID to update.")
                store_id = get_input("Store ID")
                # Retrieve store details to display and update
                store = search_store(conn, store_id)
                # Only proceed if the store was found
                if store:
                    print("What would you like to update?")
                    print("1. Store Address")
                    print("2. Phone Number")
                    print("3. Manager ID")
                    sub_choice = input("Enter choice: ")

                    # Update store address
                    if sub_choice == "1":
                        new_address = get_input("New Store Address")
                        # store[0] = StoreID, store[1] = ManagerID, store[2] = StoreAddress, store[3] = PhoneNumber
                        update_store(conn, store[0], new_address, store[3], store[1])

                    # Update phone number
                    elif sub_choice == "2":
                        new_phone_number = get_input("New Phone Number")
                        update_store(conn, store[0], store[2], new_phone_number, store[1])

                    # Update manager ID
                    elif sub_choice == "3":
                        new_manager_id = get_input("New Manager ID")
                        update_store(conn, store[0], store[2], store[3], new_manager_id)

                    # Handle invalid update choice
                    else:
                        print("Invalid choice. Please try again.")

            # Option 3: Delete a store
            elif sub_choice == "3":
                store_id = get_input("Store ID")
                # Delete the store with the given ID
                delete_store(conn, store_id)

            # Option 4: Search for a store
            elif sub_choice == "4":
                store_id = get_input("Store ID")
                # Search for and display store information
                search_store(conn, store_id)

        # Inventory Records menu (Product management)
        elif choice == "2":
            print("\n--- Inventory Records ---")
            print("1. Add Product")
            print("2. Update Product")
            print("3. Delete Product")
            sub_choice = input("Enter choice: ")

            # Using Python 3.10's match-case statement for cleaner code
            match sub_choice:
                # Option 1: Add a new product
                case 1:
                    # Collect all required information for a new product
                    product_id = get_input("Enter Product ID: ")
                    product_name = get_input("Enter Product Name: ")
                    QuantityInStock = get_input("Enter Quantity In Stock: ")
                    BuyPrice = get_input("Enter Buy Price: ")
                    SellPrice = get_input("Enter Sell Price: ")
                    store_id = get_input("Enter Store ID: ")
                    # Add the product to the database
                    add_product(conn, product_id, product_name, QuantityInStock, BuyPrice, SellPrice, store_id)

                # Option 2: Update an existing product
                case 2:
                    product_id = get_input("Enter Product ID: ")
                    # Retrieve product details to display and update
                    product = get_product(conn, product_id)
                    # Only proceed if the product was found
                    if product:
                        print("\n--- What would you like to update? ---")
                        print("1. Product Name")
                        print("2. Quantity In Stock")
                        print("3. Buy Price")
                        print("4. Sell Price")
                        print("5. Store ID")
                        update_choice = input("Enter choice: ")

                        # Using another match-case for update options
                        match update_choice:
                            # Update product name
                            case 1:
                                product_name = get_input("Enter new Product Name: ")
                                # product[0] = ProductID, product[1] = ProductName, product[2] = QuantityInStock,
                                # product[3] = BuyPrice, product[4] = SellPrice, product[5] = StoreID
                                update_product(conn, product[0], product_name, product[2], product[3], product[4],
                                               product[5])

                            # Update quantity in stock
                            case 2:
                                QuantityInStock = get_input("Enter new Quantity In Stock: ")
                                update_product(conn, product[0], product[1], product[2], QuantityInStock, product[4],
                                               product[5])

                            # Update buy price
                            case 3:
                                BuyPrice = get_input("Enter new Buy Price: ")
                                update_product(conn, product[0], product[1], product[2], BuyPrice, product[4],
                                               product[5])

                            # Update sell price
                            case 4:
                                SellPrice = get_input("Enter new Sell Price: ")
                                update_product(conn, product[0], product[1], product[2], product[3], SellPrice,
                                               product[5])

                            # Update store ID
                            case 5:
                                store_id = get_input("Enter new Store ID: ")
                                update_product(conn, product[0], product[1], product[2], product[3], product[4],
                                               store_id)

                            # Handle invalid update choice
                            case _:
                                print("Invalid choice. Please try again.")

                # Option 3: Delete a product
                case 3:
                    product_id = get_input("Enter Product ID: ")
                    # Display product information before deletion
                    get_product(conn, product_id)
                    # Confirm deletion
                    print("\n--- Are you sure you want to delete this product? ---")
                    update_choice = input("Enter 'yes' to confirm: ")
                    match update_choice:
                        case "yes":
                            # Delete the product if confirmed
                            delete_product(conn, product_id)
                            print("Product deleted successfully.")
                        case "no":
                            # Cancel deletion
                            print("Product deletion cancelled.")
                        case _:
                            # Handle invalid input
                            print("Invalid choice. Please try again.")

                # Handle invalid product menu choice
                case _:
                    print("Invalid choice. Please try again.")

            # Note: This section is marked as a placeholder for additional inventory functions

        # Billing and Transaction Records menu (placeholder)
        elif choice == "3":
            print("\n--- Billing and Transaction Records ---")
            print("1. Add Transaction")
            print("2. Add Product to Transaction")
            print("3. Calculate Transaction Total")
            sub_choice = input("Enter choice: ")
            # This section is a placeholder for future billing functionality
            # Would implement transaction creation, adding products to transactions, etc.
            print("This functionality is not yet implemented.")

        # Reports menu (placeholder)
        elif choice == "4":
            print("\n--- Reports ---")
            print("1. Monthly Customer Activity Report")
            print("2. Annual Sales Report")
            print("3. Product Stock Report")
            sub_choice = input("Enter choice: ")
            # This section is a placeholder for future reporting functionality
            # Would implement generation of various business reports
            print("This functionality is not yet implemented.")

        # Exit the program
        elif choice == "0":
            print("Exiting...")
            break

        # Handle invalid main menu choice
        else:
            print("Invalid choice. Please try again.")

    # Close the database connection when exiting the program
    conn.close()

if __name__ == "__main__":
    main()
