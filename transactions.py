from database import add_products_to_transaction, get_transaction, get_transaction_price, add_transaction


def transactions(conn):
    print("1. Add Transaction")
    print("2. Add Product to Transaction")
    print("3. Calculate Transaction Total")
    sub_choice = int(input("Enter choice: "))

    # Using match-case to handle transaction menu options
    match sub_choice:
        # Option 1: Add a new transaction
        # Creates a new transaction record with customer, store, and cashier info
        case 1:
            # Collect all required information for a new transaction
            storeid = int(input("Enter Store ID: "))  # Store where transaction occurred
            customerid = int(input("Enter Customer ID: "))  # Customer who made the purchase
            cashierid = int(input("Enter Cashier ID: "))  # Staff who processed the transaction
            purchasedate = input("Enter Purchase Date: ")  # Date of purchase
            totalprice = float(input("Total Price: "))  # Initial total price
            Transactiontype = input("Transaction Type: ")  # Buy or Return

            # Add the transaction to the database and display the generated ID
            print("Transaction id: " + str(
                add_transaction(conn, storeid, customerid, cashierid, purchasedate, totalprice, Transactiontype)))

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
                    'product_id': product_id,  # The product identifier
                    'quantity': quantity,  # How many units were purchased
                    'discount': discount  # Discount percentage applied
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
            print("Transaction Total: " + str(totalprice))

            # Handle invalid transaction menu choice with wildcard pattern match
            # Provides feedback if user enters an unrecognized option
        case _:
            print("Invalid choice. Please try again.")