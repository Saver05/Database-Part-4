

def staff(conn):
    print("1. Add Staff")
    print("2. Update Staff")
    print("3. Delete Staff")
    print("4. Search Staff")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            StaffID = int(input("Enter Staff ID: "))
            StoreId = int(input("Enter Store ID: "))
            Name = input("Enter Name: ")
            Age = int(input("Enter Age: "))
            HomeAddress = input("Enter home address: ")
            PhoneNumber = input("Enter phone number: ")
            Email = input("Enter email: ")
            StartDate = input("Enter start date (YYYY-MM-DD): ")
            create_staff(conn,StaffID, StoreId, Name, Age, HomeAddress, PhoneNumber, Email, StartDate)
        case 2:
            staff_data = search_staff(conn,input("Enter Staff ID: "))
            if not staff_data:
                print("No staff found")
                return
            staff = list(staff_data)
            print("What would you like to update?")
            print("1. Store ID")
            print("2. Name")
            print("3. Age")
            print("4. Home Address")
            print("5. Phone Number")
            print("6. Email")
            print("7. Start Date")
            choice = int(input("Enter choice: "))
            match choice:
                case 1:
                    staff[1] = int(input("Enter new Store ID: "))
                case 2:
                    staff[2] = input("Enter new Name: ")
                case 3:
                    staff[3] = int(input("Enter new Age: "))
                case 4:
                    staff[4] = input("Enter new Home Address: ")
                case 5:
                    staff[5] = input("Enter new Phone Number: ")
                case 6:
                    staff[6] = input("Enter new Email: ")
                case 7:
                    staff[7] = input("Enter new Start Date: ")
            update_staff(conn, staff[0],staff[1],staff[2],staff[3],staff[4],staff[5],staff[6],staff[7])
        case 3:
            delete_staff(conn,input("Enter Staff ID: "))
        case 4:
            search_staff(conn,input("Enter Staff ID: "))

def update_staff(conn, StaffID, StoreId, Name, Age, HomeAddress, PhoneNumber, Email, StartDate):
    try:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE Staff SET StoreId = %s, Name = %s, Age = %s, HomeAddress = %s, PhoneNumber = %s, Email = %s, StartDate = %s WHERE StaffID = %s",
                           (StoreId, Name, Age, HomeAddress, PhoneNumber, Email, StartDate, StaffID))
            conn.commit()
            print("Staff updated successfully.")
    except Exception as e:
        print(f"Error updating staff: {e}")

def delete_staff(conn,StaffID):
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM Staff WHERE StaffID = %s", (StaffID,))
            conn.commit()
            print("Staff deleted successfully.")
    except Exception as e:
        print(f"Error deleting staff: {e}")

def search_staff(conn, StaffID):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Staff WHERE StaffID = %s", (StaffID,))
            staff = cursor.fetchone()
            if staff:
                print(staff)
                return staff
            else:
                print("Staff not found.")
                return None
    except Exception as e:
        print(f"Error searching for staff: {e}")
        return None

def create_staff(conn, StaffID, StoreId, Name, Age, HomeAddress, PhoneNumber, Email, StartDate):
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO Staff (StaffID, StoreId, Name, Age, HomeAddress, PhoneNumber, Email, StartDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                           (StaffID, StoreId, Name, Age, HomeAddress, PhoneNumber, Email, StartDate))
            conn.commit()
            print("Staff created successfully.")
    except Exception as e:
        print(f"Error creating staff: {e}")