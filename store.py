from database import get_input, add_store, search_store, update_store, delete_store


def store(conn):
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
        phone_number = get_input("Phone Number")  # Get the phone number from user
        manager_id = get_input("Manager ID")  # Get the manager ID from user

        # Add the store to the database using the collected information
        # The add_store function is defined in database.py
        add_store(conn, store_address, phone_number, manager_id)

    # Option 2: Update an existing store
    # Allows modifying store details like address, phone number, and manager
    elif sub_choice == "2":
        print("Enter the store ID to update.")
        store_id = int(get_input("Store ID"))  # Get ID of store to update

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
        store_id = int(input("Store ID"))  # Get ID of store to delete
        # Delete the store with the given ID from the database
        delete_store(conn, store_id)

    # Option 4: Search for a store
    # Retrieves and displays store information by ID
    elif sub_choice == "4":
        store_id = int(get_input("Store ID"))  # Get ID of store to search for
        # Search for and display store information
        # search_store handles both retrieval and display of the store data
        search_store(conn, store_id)

    # Handle invalid store menu choice
    else:
        print("Invalid option please try again.")