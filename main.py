# main.py
from database import add_store, update_store, delete_store, search_store, get_input, connect_to_database

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
                store_address = get_input("Store Address")  # Get store address from user input
                location = get_input("Location")  # Get location from user input
                # Assuming StoreID, ManagerID, StoreAddress, PhoneNumber are provided
                add_store(conn, store_address, location)  # Call the add_store function
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
