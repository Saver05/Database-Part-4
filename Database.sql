-- Drop in need
DROP DATABASE IF EXISTS `MuskieCo`;
-- Create the database
CREATE DATABASE MuskieCo;
USE MuskieCo;

-- Store Table
CREATE TABLE Store (
    StoreID INT AUTO_INCREMENT PRIMARY KEY,
    ManagerID INT UNIQUE,
    StoreAddress VARCHAR(255) NOT NULL UNIQUE,
    PhoneNumber VARCHAR(15) UNIQUE
);

-- Staff Table
CREATE TABLE Staff (
    StaffID INT PRIMARY KEY,
    StoreID INT,
    Name VARCHAR(100) NOT NULL,
    Age INT CHECK (Age >= 18),
    HomeAddress VARCHAR(255) NOT NULL,
    PhoneNumber VARCHAR(15) UNIQUE,
    Email VARCHAR(100) UNIQUE,
    StartDate DATE,
    FOREIGN KEY (StoreID) REFERENCES Store(StoreID) ON DELETE SET NULL
);

-- Customer Table
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    PhoneNumber VARCHAR(15) UNIQUE,
    HomeAddress VARCHAR(255),
    IsActive BOOLEAN DEFAULT TRUE,
    SignUpDate DATE,
    RewardPoints INT CHECK (RewardPoints >= 0)
);

-- CustomerSignUp Table
CREATE TABLE CustomerSignUp (
    SignUpStaffID INT,
    CustomerID INT,
    SignUpDate DATE,
    PRIMARY KEY (SignUpStaffID, CustomerID),
    FOREIGN KEY (SignUpStaffID) REFERENCES Staff(StaffID) ON DELETE CASCADE,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID) ON DELETE CASCADE
);

-- Product Table
CREATE TABLE Product (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    QuantityInStock INT CHECK (QuantityInStock >= 0),
    BuyPrice DECIMAL(10,2) CHECK (BuyPrice >= 0),
    SellPrice DECIMAL(10,2) CHECK (SellPrice >= 0),
    StoreID INT,
    FOREIGN KEY (StoreID) REFERENCES Store(StoreID) ON DELETE CASCADE
);

-- Transaction Table
CREATE TABLE Transaction (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,
    StoreID INT,
    CustomerID INT,
    CashierID INT,
    PurchaseDate DATE NOT NULL,
    TotalPrice DECIMAL(10,2) CHECK (TotalPrice >= 0),
    TransactionType ENUM('Buy', 'Return') NOT NULL,
    FOREIGN KEY (StoreID) REFERENCES Store(StoreID) ON DELETE SET NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID) ON DELETE SET NULL,
    FOREIGN KEY (CashierID) REFERENCES Staff(StaffID) ON DELETE SET NULL
);

-- Discount Table
CREATE TABLE Discount (
    DiscountID INT PRIMARY KEY,
    ProductID INT,
    StoreID INT,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (StoreID) REFERENCES Store(StoreID) ON DELETE CASCADE
);

-- DiscountDetails Table
CREATE TABLE DiscountDetails (
    ProductID INT,
    StoreID INT,
    DiscountPercentage DECIMAL(5,2) CHECK (DiscountPercentage >= 0 AND DiscountPercentage <= 100),
    ValidFrom DATE NOT NULL,
    ValidTo DATE NOT NULL,
    PRIMARY KEY (ProductID, StoreID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (StoreID) REFERENCES Store(StoreID) ON DELETE CASCADE
);

-- TransactionItem Table
CREATE TABLE TransactionItem (
    TransactionID INT,
    ProductID INT,
    Quantity INT CHECK (Quantity > 0) NOT NULL,
    DiscountPercentageApplied DECIMAL(5,2) CHECK (DiscountPercentageApplied >= 0 AND DiscountPercentageApplied <= 100),
    PRIMARY KEY (TransactionID, ProductID),
    FOREIGN KEY (TransactionID) REFERENCES Transaction(TransactionID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID) ON DELETE CASCADE
);

-- Part 2: INSERT Statements

-- Insert into Store
INSERT INTO Store (StoreID, ManagerID, StoreAddress, PhoneNumber) VALUES
(1, 101, '123 Main St, Raleigh, NC', '919-555-1111'),
(2, 102, '456 Oak St, Charlotte, NC', '704-555-2222'),
(3, 103, '789 Pine St, Durham, NC', '984-555-3333'),
(4, 104, '101 Maple Ave, Cary, NC', '919-555-4444'),
(5, 105, '202 Birch Rd, Apex, NC', '984-555-5555');

-- Insert into Staff
INSERT INTO Staff (StaffID, StoreID, Name, Age, HomeAddress, PhoneNumber, Email, StartDate) VALUES
(101, 1, 'Alice Johnson', 30, '500 Elm St, Raleigh, NC', '919-555-6001', 'alice@example.com', '2020-06-15'),
(102, 2, 'Bob Smith', 28, '750 Oak St, Charlotte, NC', '704-555-6002', 'bob@example.com', '2021-03-22'),
(103, 3, 'Charlie Brown', 35, '850 Pine St, Durham, NC', '984-555-6003', 'charlie@example.com', '2019-11-10'),
(104, 4, 'David Wilson', 40, '950 Maple Ave, Cary, NC', '919-555-6004', 'david@example.com', '2018-08-05'),
(105, 5, 'Eve Adams', 27, '650 Birch Rd, Apex, NC', '984-555-6005', 'eve@example.com', '2022-01-18');

-- Insert into Customer
INSERT INTO Customer (CustomerID, FirstName, LastName, Email, PhoneNumber, HomeAddress, IsActive, SignUpDate, RewardPoints) VALUES
(1, 'John', 'Doe', 'john@example.com', '919-555-7001', '100 Cedar St, Raleigh, NC', TRUE, '2023-01-01', 50),
(2, 'Sarah', 'Lee', 'sarah@example.com', '704-555-7002', '200 Pine St, Charlotte, NC', TRUE, '2023-02-15', 120),
(3, 'Mike', 'Davis', 'mike@example.com', '984-555-7003', '300 Oak St, Durham, NC', FALSE, '2022-12-10', 0),
(4, 'Laura', 'Harris', 'laura@example.com', '919-555-7004', '400 Maple Ave, Cary, NC', TRUE, '2023-03-05', 75),
(5, 'Tom', 'Anderson', 'tom@example.com', '984-555-7005', '500 Birch Rd, Apex, NC', TRUE, '2023-04-20', 30);

-- Insert into CustomerSignUp
INSERT INTO CustomerSignUp (SignUpStaffID, CustomerID, SignUpDate) VALUES
(101, 1, '2023-01-01'),
(102, 2, '2023-02-15'),
(103, 3, '2022-12-10'),
(104, 4, '2023-03-05'),
(105, 5, '2023-04-20');

-- Insert into Product
INSERT INTO Product (ProductID, ProductName, QuantityInStock, BuyPrice, SellPrice, StoreID) VALUES
(1, 'Laptop', 10, 500.00, 700.00, 1),
(2, 'Smartphone', 15, 300.00, 500.00, 2),
(3, 'Headphones', 25, 50.00, 100.00, 3),
(4, 'Monitor', 8, 150.00, 250.00, 4),
(5, 'Keyboard', 20, 20.00, 50.00, 5);

-- Insert into Discount
INSERT INTO Discount (DiscountID, ProductID, StoreID) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5);

-- Insert into DiscountDetails
INSERT INTO DiscountDetails (ProductID, StoreID, DiscountPercentage, ValidFrom, ValidTo) VALUES
(1, 1, 10.00, '2024-01-01', '2024-03-01'),
(2, 2, 15.00, '2024-02-01', '2024-04-01'),
(3, 3, 5.00, '2024-03-01', '2024-05-01'),
(4, 4, 20.00, '2024-04-01', '2024-06-01'),
(5, 5, 8.00, '2024-05-01', '2024-07-01');

-- Insert into Transaction
INSERT INTO Transaction (TransactionID, StoreID, CustomerID, CashierID, PurchaseDate, TotalPrice, TransactionType) VALUES
(1, 1, 1, 101, '2024-03-05', 700.00, 'Buy'),
(2, 2, 2, 102, '2024-03-10', 500.00, 'Buy'),
(3, 3, 3, 103, '2024-03-15', 100.00, 'Buy'),
(4, 4, 4, 104, '2024-03-20', 250.00, 'Buy'),
(5, 5, 5, 105, '2024-03-25', 50.00, 'Return');

-- Insert into TransactionItem
INSERT INTO TransactionItem (TransactionID, ProductID, Quantity, DiscountPercentageApplied) VALUES
(1, 1, 1, 10.00),
(2, 2, 1, 15.00),
(3, 3, 1, 5.00),
(4, 4, 1, 20.00),
(5, 5, 1, 8.00);
