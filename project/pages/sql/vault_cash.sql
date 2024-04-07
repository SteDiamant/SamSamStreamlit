CREATE TABLE IF NOT EXISTS vault_cash (
    id INTEGER NOT NULL, 
    amount100 INTEGER, 
    amount50 INTEGER, 
    amount20 INTEGER, 
    amount10 INTEGER, 
    amount5 INTEGER, 
    amount2 INTEGER, 
    amount1 INTEGER, 
    amount050 INTEGER, 
    amount020 INTEGER, 
    amount010 INTEGER, 
    amount005 INTEGER, 
    date DATE NULL, 
    updated_date DATE NOT NULL, 
    PRIMARY KEY (id)
);

INSERT INTO vault_cash (id, amount100, amount50, amount20, amount10, amount5, amount2, amount1, amount050, amount020, amount010, amount005, date, updated_date)
VALUES
    (1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, '2024-04-01', DATE('now')),
    (2, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, '2024-04-02', DATE('now')),
    (3, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, '2024-04-03', DATE('now')),
    (4, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, '2024-04-04', DATE('now')),
    (5, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, '2024-04-05', DATE('now')),
    (6, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, '2024-04-06', DATE('now')),
    (7, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, '2024-04-07', DATE('now')),
    (8, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, '2024-04-08', DATE('now')),
    (9, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, '2024-04-09', DATE('now')),
    (10, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, '2024-04-10', DATE('now')),
    (11, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, '2024-04-11', DATE('now')),
    (12, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, '2024-04-12', DATE('now')),
    (13, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, '2024-04-13', DATE('now')),
    (14, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, '2024-04-14', DATE('now')),
    (15, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, '2024-04-15', DATE('now'));
