
CREATE TABLE external_payment (
    id INTEGER NOT NULL, 
    source VARCHAR(200), 
    amount FLOAT NOT NULL, 
    description VARCHAR(500), 
    date DATE NOT NULL, 
    updated_date DATE NOT NULL, 
    PRIMARY KEY (id)
);

INSERT INTO external_payment (id, source, amount, description, date, updated_date)
VALUES
    (1, 'Bank A', 100.50, 'Payment for services', '2024-04-01', '2024-04-01'),
    (2, 'Bank B', 150.25, 'Product purchase', '2024-04-02', '2024-04-02'),
    (3, 'Bank C', 75.80, 'Subscription renewal', '2024-04-03', '2024-04-03'),
    (4, 'Bank D', 200.00, 'Loan repayment', '2024-04-04', '2024-04-04'),
    (5, 'Bank E', 85.60, 'Purchase of equipment', '2024-04-05', '2024-04-05'),
    (6, 'Bank F', 120.75, 'Invoice payment', '2024-04-06', '2024-04-06'),
    (7, 'Bank G', 300.30, 'Consultation fee', '2024-04-07', '2024-04-07'),
    (8, 'Bank H', 50.00, 'Donation', '2024-04-08', '2024-04-08'),
    (9, 'Bank I', 90.20, 'Service charge', '2024-04-09', '2024-04-09'),
    (10, 'Bank J', 175.90, 'Product purchase', '2024-04-10', '2024-04-10'),
    (11, 'Bank K', 120.00, 'Invoice payment', '2024-04-11', '2024-04-11'),
    (12, 'Bank L', 80.50, 'Consultation fee', '2024-04-12', '2024-04-12'),
    (13, 'Bank M', 95.75, 'Service charge', '2024-04-13', '2024-04-13'),
    (14, 'Bank N', 150.60, 'Payment for services', '2024-04-14', '2024-04-14'),
    (15, 'Bank O', 110.25, 'Product purchase', '2024-04-15', '2024-04-15');
