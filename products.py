from database import get_input, get_product, delete_product, update_product, add_product


def products(conn):
    # Display the product management submenu
    print("\n--- Inventory Records ---")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. View Product")
    sub_choice = int(input("Enter choice: "))

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
                update_choice = int(input("Enter choice: "))

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
                        QuantityInStock = int(get_input("Enter new Quantity In Stock: "))
                        # Keep other fields the same, only update the quantity
                        update_product(conn, product[0], product[1], QuantityInStock, product[3], product[4],
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
        case 4:
            get_product(conn, get_input("Enter Product ID: "))
        # Handle invalid product menu choice with wildcard pattern match
        case _:
            print("Invalid choice. Please try again.")
