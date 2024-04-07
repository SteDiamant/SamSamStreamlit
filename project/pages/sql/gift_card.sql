CREATE TABLE IF NOT EXISTS gift_card (
    id INTEGER NOT NULL, 
    source VARCHAR(200), 
    amount FLOAT NOT NULL, 
    description VARCHAR(500), 
    date DATE NOT NULL, 
    updated_date DATE NOT NULL, 
    PRIMARY KEY (id)
);

INSERT INTO gift_card (id, source, amount, description, date, updated_date)
VALUES
    (1, 'Online Store A', 50.00, 'Gift card purchase', '2024-04-01 12:00:00', '2024-04-01 12:00:00'),
    (2, 'Retail Store B', 100.00, 'Gift card redemption', '2024-04-02 10:30:00', '2024-04-02 10:30:00'),
    (3, 'Online Store C', 25.00, 'Gift card purchase', '2024-04-03 15:45:00', '2024-04-03 15:45:00'),
    (4, 'Retail Store D', 75.00, 'Gift card redemption', '2024-04-04 08:00:00', '2024-04-04 08:00:00'),
    (5, 'Online Store E', 20.00, 'Gift card purchase', '2024-04-05 14:20:00', '2024-04-05 14:20:00'),
    (6, 'Retail Store F', 50.00, 'Gift card redemption', '2024-04-06 11:10:00', '2024-04-06 11:10:00'),
    (7, 'Online Store G', 30.00, 'Gift card purchase', '2024-04-07 09:30:00', '2024-04-07 09:30:00'),
    (8, 'Retail Store H', 80.00, 'Gift card redemption', '2024-04-08 16:00:00', '2024-04-08 16:00:00'),
    (9, 'Online Store I', 35.00, 'Gift card purchase', '2024-04-09 13:45:00', '2024-04-09 13:45:00'),
    (10, 'Retail Store J', 60.00, 'Gift card redemption', '2024-04-10 10:00:00', '2024-04-10 10:00:00'),
    (11, 'Online Store K', 45.00, 'Gift card purchase', '2024-04-11 11:30:00', '2024-04-11 11:30:00'),
    (12, 'Retail Store L', 70.00, 'Gift card redemption', '2024-04-12 09:15:00', '2024-04-12 09:15:00'),
    (13, 'Online Store M', 55.00, 'Gift card purchase', '2024-04-13 14:40:00', '2024-04-13 14:40:00'),
    (14, 'Retail Store N', 90.00, 'Gift card redemption', '2024-04-14 12:45:00', '2024-04-14 12:45:00'),
    (15, 'Online Store O', 40.00, 'Gift card purchase', '2024-04-15 10:20:00', '2024-04-15 10:20:00');
