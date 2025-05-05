
def customer_rewards(conn):
    customer_id = input("Enter customer id: ")
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT RewardPoints FROM Customer WHERE CustomerID = %s", (customer_id,))
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

def employee_rewards(conn):
    employee_id = input("Enter employee id: ")
    month = input("Enter month: ")
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT Count(CustomerID) FROM CustomerSignUp WHERE SignUpStaffID = %s", employee_id)
            rewards = cursor.fetchall()
            print(rewards)
            return None
    except Exception as e:
        print(f"Error searching for employee: {e}")
        return None