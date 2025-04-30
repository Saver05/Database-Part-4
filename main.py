# main.py
from database import add_store, update_store, delete_store, search_store, get_input, connect_to_database, add_product, \
    get_product, update_product, delete_product


def main():
    conn = connect_to_database()
    while True:
        print("--- MuskieCo Main Menu ---")
        print("Which task would you like to perform?")
        print("1. Information Processing")
        print("2. Inventory Records")
        print("3. Billing and Transaction Records")
        print("4. Reports")
        print("0. Exit")
        choice = input("Enter the number corresponding to your choice: ")

        if choice == "1":
            print("\n--- Information Processing ---")
            print("1. Add Store")
            print("2. Update Store")
            print("3. Delete Store")
            print("4. Search Store")
            sub_choice = input("Enter choice: ")

            if sub_choice == "1":
                store_address = get_input("Store Address")  # Get the store address from user input
                phone_number = get_input("Phone Number")
                manager_id = get_input("Manager ID")
                add_store(conn, store_address, phone_number, manager_id)  # Call the add_store function
            elif sub_choice == "2":
                store_id = get_input("Store ID")
                new_address = get_input("New Store Address")
                update_store(conn, store_id, new_address)
            elif sub_choice == "3":
                store_id = get_input("Store ID")
                delete_store(conn, store_id)
            elif sub_choice == "4":
                store_id = get_input("Store ID")
                search_store(conn, store_id)

        elif choice == "2":
            print("\n--- Inventory Records ---")
            print("1. Add Product")
            print("2. Update Product")
            print("3. Delete Product")
            sub_choice = input("Enter choice: ")
            match sub_choice:
                case 1:
                    product_id = get_input("Enter Product ID: ")
                    product_name = get_input("Enter Product Name: ")
                    QuantityInStock = get_input("Enter Quantity In Stock: ")
                    BuyPrice = get_input("Enter Buy Price: ")
                    SellPrice = get_input("Enter Sell Price: ")
                    store_id = get_input("Enter Store ID: ")
                    add_product(conn, product_id, product_name, QuantityInStock, BuyPrice, SellPrice, store_id)
                case 2:
                    product_id = get_input("Enter Product ID: ")
                    product = get_product(conn, product_id)
                    print("\n--- What would you like to update? ---")
                    print("1. Product Name")
                    print("2. Quantity In Stock")
                    print("3. Buy Price")
                    print("4. Sell Price")
                    print("5. Store ID")
                    update_choice = input("Enter choice: ")
                    match update_choice:
                        case 1:
                            product_name = get_input("Enter new Product Name: ")
                            update_product(conn, product[0], product_name, product[2], product[3], product[4],
                                           product[5])
                        case 2:
                            QuantityInStock = get_input("Enter new Quantity In Stock: ")
                            update_product(conn, product[0], product[1], product[2], QuantityInStock, product[4],
                                           product[5])
                        case 3:
                            BuyPrice = get_input("Enter new Buy Price: ")
                            update_product(conn, product[0], product[1], product[2], BuyPrice, product[4], product[5])
                        case 4:
                            SellPrice = get_input("Enter new Sell Price: ")
                            update_product(conn, product[0], product[1], product[2], product[3], SellPrice, product[5])
                        case 5:
                            store_id = get_input("Enter new Store ID: ")
                            update_product(conn, product[0], product[1], product[2], product[3], product[4], store_id)
                        case _:
                            print("Invalid choice. Please try again.")
                case 3:
                    product_id = get_input("Enter Product ID: ")
                    get_product(conn, product_id)
                    print("\n--- Are you sure you want to delete this product? ---")
                    update_choice = input("Enter 'yes' to confirm: ")
                    match update_choice:
                        case "yes":
                            delete_product(conn, product_id)
                            print("Product deleted successfully.")
                        case "no":
                            print("Product deletion cancelled.")
                        case _:
                            print("Invalid choice. Please try again.")

            # Handle options similarly for inventory-related tasks...

        elif choice == "3":
            print("\n--- Billing and Transaction Records ---")
            print("1. Add Transaction")
            print("2. Add Product to Transaction")
            print("3. Calculate Transaction Total")
            sub_choice = input("Enter choice: ")
            # Handle options similarly for billing and transaction-related tasks...

        elif choice == "4":
            print("\n--- Reports ---")
            print("1. Monthly Customer Activity Report")
            print("2. Annual Sales Report")
            print("3. Product Stock Report")
            sub_choice = input("Enter choice: ")
            # Handle options similarly for report-related tasks...

        elif choice == "0":
            print("Exiting...")
            break

    conn.close()

if __name__ == "__main__":
    main()
