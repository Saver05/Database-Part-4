
def discount(conn):
    print("1. Add Discount")
    print("2. Update Discount")
    print("3. Delete Discount")
    print("4. View Discount")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            discount_id = int(input("Enter Discount ID: "))
            product_id = int(input("Enter Product ID: "))
            store_id = int(input("Enter Store ID: "))
            add_discount(conn,discount_id,product_id,store_id)
        case 2:
            discount_id = int(input("Enter Discount ID: "))
            discount_data = search_discount(conn,discount_id)
            discount = list(discount_data)
            print("What would you like to update?")
            print("1. Product ID")
            print("2. Store ID")
            match int(input("Enter choice: ")):
                case 1:
                    discount[1] = int(input("Enter new Product ID: "))
                case 2:
                    discount[2] = int(input("Enter new Store ID: "))
            update_discount(conn,discount_id,discount[1],discount[2])
        case 3:
            delete_discount(conn,input("Enter Discount ID: "))
        case 4:
            discount_id = int(input("Enter Discount ID: "))
            search_discount(conn,discount_id)
        case _:
            print("Invalid choice. Please try again.")


def delete_discount(conn, discount_id):
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM Discount WHERE DiscountID = %s", (discount_id,))
            conn.commit()
            print("Discount deleted successfully.")
    except Exception as e:
        print(f"Error deleting discount: {e}")

def update_discount(conn, discount_id, product_id, store_id):
    try:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE Discount SET ProductID = %s, StoreID = %s WHERE DiscountID = %s",
                           (product_id, store_id, discount_id))
            conn.commit()
            print("Discount updated successfully.")
    except Exception as e:
        print(f"Error updating discount: {e}")

def search_discount(conn, discount_id):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Discount WHERE DiscountID = %s", (discount_id,))
            discount = cursor.fetchone()
            if discount:
                print(discount)
                return discount
            else:
                print("Discount not found.")
                return None
    except Exception as e:
        print(f"Error searching for discount: {e}")
        return None

def add_discount(conn, discount_id, product_id, store_id):
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO Discount (DiscountID, ProductID, StoreID) VALUES (%s, %s, %s)",
                           (discount_id, product_id, store_id))
            conn.commit()
            print("Discount added successfully.")
    except Exception as e:
        print(f"Error adding discount: {e}")