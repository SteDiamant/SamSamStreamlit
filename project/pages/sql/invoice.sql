CREATE TABLE IF NOT EXISTS invoice (
    id INTEGER NOT NULL, 
    contact VARCHAR(200) NOT NULL, 
    email VARCHAR(200) NOT NULL, 
    amount FLOAT NOT NULL, 
    bussiness_name VARCHAR(200) NOT NULL, 
    bussiness_code VARCHAR(200) NOT NULL, 
    description VARCHAR(500) NOT NULL, 
    status VARCHAR(200) NOT NULL, 
    date DATE NOT NULL, 
    updated_date DATE NOT NULL, 
    PRIMARY KEY (id)
);
INSERT INTO invoice (id, contact, email, amount, bussiness_name, bussiness_code, description, status, date, updated_date)
VALUES
    (1, 'John Doe', 'john@example.com', 100.00, 'ABC Company', 'ABC123', 'Consultation Fee', 'Paid', '2024-04-01 12:00:00', '2024-04-01 12:00:00'),
    (2, 'Jane Smith', 'jane@example.com', 150.00, 'XYZ Inc.', 'XYZ456', 'Product Purchase', 'Pending', '2024-04-02 10:30:00', '2024-04-02 10:30:00'),
    (3, 'Alice Johnson', 'alice@example.com', 75.00, 'ACME Corporation', 'ACME789', 'Service Charge', 'Paid', '2024-04-03 15:45:00', '2024-04-03 15:45:00'),
    (4, 'Bob Brown', 'bob@example.com', 200.00, '123 Industries', '123XYZ', 'Invoice Payment', 'Pending', '2024-04-04 08:00:00', '2024-04-04 08:00:00'),
    (5, 'Emily Davis', 'emily@example.com', 85.00, 'Tech Solutions', 'TECH101', 'Subscription Renewal', 'Paid', '2024-04-05 14:20:00', '2024-04-05 14:20:00'),
    (6, 'Michael Wilson', 'michael@example.com', 120.00, 'DEF Corp', 'DEF456', 'Product Purchase', 'Pending', '2024-04-06 11:10:00', '2024-04-06 11:10:00'),
    (7, 'Sarah Taylor', 'sarah@example.com', 300.00, 'GHI Enterprises', 'GHI789', 'Consultation Fee', 'Paid', '2024-04-07 09:30:00', '2024-04-07 09:30:00'),
    (8, 'Kevin Lee', 'kevin@example.com', 50.00, 'JKL Ltd.', 'JKL123', 'Donation', 'Pending', '2024-04-08 16:00:00', '2024-04-08 16:00:00'),
    (9, 'Amanda Clark', 'amanda@example.com', 90.00, 'LMN Co.', 'LMN456', 'Service Charge', 'Paid', '2024-04-09 13:45:00', '2024-04-09 13:45:00'),
    (10, 'David Martinez', 'david@example.com', 175.00, 'OPQ Group', 'OPQ789', 'Invoice Payment', 'Pending', '2024-04-10 10:00:00', '2024-04-10 10:00:00'),
    (11, 'Jennifer Anderson', 'jennifer@example.com', 120.00, 'RST Inc.', 'RST101', 'Product Purchase', 'Paid', '2024-04-11 11:30:00', '2024-04-11 11:30:00'),
    (12, 'Mark Thompson', 'mark@example.com', 80.00, 'UVW Corp', 'UVW123', 'Consultation Fee', 'Pending', '2024-04-12 09:15:00', '2024-04-12 09:15:00'),
    (13, 'Laura Harris', 'laura@example.com', 95.00, 'XYZ Ltd.', 'XYZ456', 'Service Charge', 'Paid', '2024-04-13 14:40:00', '2024-04-13 14:40:00'),
    (14, 'Steven Turner', 'steven@example.com', 150.00, 'ABC Solutions', 'ABC101', 'Invoice Payment', 'Pending', '2024-04-14 12:45:00', '2024-04-14 12:45:00'),
    (15, 'Olivia Wilson', 'olivia@example.com', 110.00, 'DEF Inc.', 'DEF789', 'Product Purchase', 'Paid', '2024-04-15 10:20:00', '2024-04-15 10:20:00');
