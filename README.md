Welcome to our CSCI 335 Databases Final Project repository!

This README will serve as an overview of our decisions in terms of code organization and the contributions of our members.

MEMBERS:
Alex Welch, Jack Frambes, Adam Maida, and Sam Fortin. Together, we gathered our experiences and worked on this project.
We each contributed aspects revolving around the creation of the database, SQL statements, and API creation. This projects
code was a collaborated effort.

ORGANIZATION:
Application Portion (main.py):
  We Provided a menu interface for users to interact with the system like introduced in the project description.
  Separated tasks into groups:
    Information Processing (e.g., managing stores)
    Inventory Records (e.g., managing products)
    Billing/Transaction Records
    Reports
  This handles user inputs, then delegates database work to file database.py

Database Portion (database.py):
  Groups all SQL logic and database connection setup.
  Specifies database operations such as add_store, update_store, etc.
  Prevent injection (malicious inputs) and added security.
  Reads and executes a complete schema from Database.sql, making the program easy to run.

Schema Portion (Database.sql):
  Uses our relational schema with keys and constraints to preserve data.
  Supports discounts and reward points with tables (Discount, CustomerSignUp, etc.)

Additional Information (store.py, customer.py, etc.)
  Files added titled by respective entity created for specific operations based on overview.

These coding decisions helped us in the development process of our final project.
  
