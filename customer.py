

def customer(conn):
    print("1. Add Customer")
    print("2. Update Customer")
    print("3. Delete Customer")
    print("4. Find Customer")
    choice = input("Enter the number corresponding to your choice: ")
    match choice:
        case "1":
            CustomerID = int(input("Enter Customer ID: "))
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            phonenumber = input("Enter phone number: ")
            homeaddress = input("Enter home address: ")
            isActive = True
            signupdate = input("Enter date of signup (YYYY-MM-DD): ")
            rewardspoints = 0
            create_customer(conn,CustomerID, first_name, last_name, email, phonenumber, homeaddress, isActive, signupdate, rewardspoints)
        case "2":
            customer_data = search_customer(conn,int(input("Enter Customer ID: ")))
            if not customer_data:
                print("No Customer found")
                return
            customer = list(customer_data)
            print("What would you like to update?")
            print("1. First Name")
            print("2. Last Name")
            print("3. Email")
            print("4. Phone Number")
            print("5. Home Address")
            print("6. Is Active")
            print("7. Signup Date")
            print("8. Reward Points")
            choice = input("Enter choice: ")
            match choice:
                case "1":
                    customer[1] = input("Enter new first name: ")
                case "2":
                    customer[2] = input("Enter new last name: ")
                case "3":
                    customer[3] = input("Enter new email: ")
                case "4":
                    customer[4] = input("Enter new phone number: ")
                case "5":
                    customer[5] = input("Enter new home address: ")
                case "6":
                    customer[6] = True if input("Enter 'True' to activate, 'False' to deactivate: ") == "True" else False
                case "7":
                    customer[7] = input("Enter new signup date (YYYY-MM-DD): ")
                case "8":
                    customer[8] = int(input("Enter new reward points: "))
            update_customer(conn, customer[0],customer[1],customer[2],customer[3],customer[4],customer[5],customer[6],customer[7],customer[8])
        case "3":
            delete_customer(conn,int(input("Enter Customer ID: ")))
        case "4":
            search_customer(conn,int(input("Enter Customer ID: ")))

def update_customer(conn, CustomerID, first_name, last_name, email, phonenumber, homeaddress, isActive, signupdate, rewardspoints):
    try:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE Customer SET FirstName = %s, LastName = %s, Email = %s, PhoneNumber = %s, HomeAddress = %s, IsActive = %s, SignUpdate = %s, RewardPoints = %s WHERE CustomerID = %s",
                           (first_name, last_name, email, phonenumber, homeaddress, isActive, signupdate, rewardspoints, CustomerID))
            conn.commit()
            print("Customer updated successfully.")
    except Exception as e:
        print(f"Error updating customer: {e}")

def delete_customer(conn,CustomerID):
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM Customer WHERE CustomerID = %s", (CustomerID,))
            conn.commit()
            print("Customer deleted successfully.")
    except Exception as e:
        print(f"Error deleting customer: {e}")

def search_customer(conn,CustomerID):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Customer WHERE CustomerID = %s", (CustomerID,))
            customer = cursor.fetchone()
            if customer:
                print(customer)
                return customer
            else:
                print("Customer not found.")
                return None
    except Exception as e:
        print(f"Error searching for customer: {e}")
        return None

def create_customer(conn,CustomerID, first_name, last_name, email, phonenumber, homeaddress, isActive, signupdate, rewardspoints):
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO Customer (CustomerID,FirstName, LastName, Email, PhoneNumber, HomeAddress, IsActive, SignUpdate, RewardPoints) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                           ,(CustomerID, first_name, last_name, email, phonenumber, homeaddress, isActive, signupdate, rewardspoints))
            conn.commit()
            print("Customer created successfully.")
    except Exception as e:
        print(f"Error creating customer: {e}")