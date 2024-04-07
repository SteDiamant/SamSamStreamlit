CREATE TABLE IF NOT EXISTS kassa_strook (
    id INTEGER NOT NULL, 
    "Hoofdgerechten_8000" FLOAT, 
    "Nagerechten_8030" FLOAT, 
    "Gebak_8040" FLOAT, 
    "Kleine_kaart_8010" FLOAT, 
    "Dagschotels_8020" FLOAT, 
    "Dranken_hoog_8100" FLOAT, 
    "Frisdranken_overig_8200" FLOAT, 
    "Koffie_8300" FLOAT, 
    "Cultuurkaarten_4760" FLOAT, 
    "Dagschotelabonnementer_2200" FLOAT, 
    "Omzet_kadobonnen_2220" FLOAT, 
    "Catering_8050" FLOAT, 
    "Zaalhuur_8400" FLOAT, 
    date DATE NOT NULL, 
    updated_date DATE NOT NULL, 
    PRIMARY KEY (id)
);
INSERT INTO kassa_strook (id, "Hoofdgerechten_8000", "Nagerechten_8030", "Gebak_8040", "Kleine_kaart_8010", "Dagschotels_8020", "Dranken_hoog_8100", "Frisdranken_overig_8200", "Koffie_8300", "Cultuurkaarten_4760", "Dagschotelabonnementer_2200", "Omzet_kadobonnen_2220", "Catering_8050", "Zaalhuur_8400", date, updated_date)
VALUES
    (1, 120.50, 45.75, 30.25, 80.00, 65.25, 150.00, 75.50, 40.25, 95.00, 110.75, 65.50, 90.25, 100.00, '2024-04-01 12:00:00', '2024-04-01 12:00:00'),
    (2, 110.25, 40.50, 35.75, 75.00, 60.50, 140.25, 70.75, 45.00, 90.25, 105.50, 60.75, 85.25, 95.50, '2024-04-02 10:30:00', '2024-04-02 10:30:00'),
    (3, 115.75, 50.25, 25.50, 85.00, 70.25, 160.75, 80.50, 35.75, 100.25, 115.50, 70.25, 95.75, 105.00, '2024-04-03 15:45:00', '2024-04-03 15:45:00'),
    (4, 125.00, 60.75, 20.25, 90.00, 75.75, 165.00, 85.25, 50.50, 105.00, 120.25, 75.00, 100.25, 110.50, '2024-04-04 08:00:00', '2024-04-04 08:00:00'),
    (5, 130.25, 55.50, 27.00, 95.00, 80.50, 170.25, 90.00, 55.75, 110.50, 125.75, 80.25, 105.50, 115.75, '2024-04-05 14:20:00', '2024-04-05 14:20:00'),
    (6, 135.50, 65.25, 22.75, 100.00, 85.25, 175.50, 95.75, 60.00, 115.75, 130.00, 85.50, 110.75, 120.00, '2024-04-06 11:10:00', '2024-04-06 11:10:00'),
    (7, 140.75, 70.00, 18.50, 105.00, 90.00, 180.75, 100.50, 65.25, 120.00, 135.25, 90.75, 115.00, 125.25, '2024-04-07 09:30:00', '2024-04-07 09:30:00'),
    (8, 145.00, 75.75, 24.25, 110.00, 95.75, 185.00, 105.25, 70.50, 125.25, 140.50, 95.00, 120.25, 130.50, '2024-04-08 16:00:00', '2024-04-08 16:00:00'),
    (9, 150.25, 80.50, 30.00, 115.00, 100.50, 190.25, 110.00, 75.75, 130.50, 145.75, 100.25, 125.50, 135.75, '2024-04-09 13:45:00', '2024-04-09 13:45:00'),
    (10, 155.50, 85.25, 35.75, 120.00, 105.25, 195.50, 115.75, 80.00, 135.75, 150.00, 105.50, 130.75, 140.00, '2024-04-10 10:00:00', '2024-04-10 10:00:00'),
    (11, 160.75, 90.00, 41.50, 125.00, 110.00, 200.75, 120.50, 85.25, 140.00, 155.25, 110.25, 135.00, 145.25, '2024-04-11 11:30:00', '2024-04-11 11:30:00'),
    (12, 165.00, 95.75, 47.25, 130.00, 115.75, 205.00, 125.25, 90.50, 145.25, 160.50, 115.00, 140.25, 150.50, '2024-04-12 09:15:00', '2024-04-12 09:15:00'),
    (13, 170.25, 100.50, 53.00, 135.00, 120.50, 210.25, 130.00, 95.75, 150.50, 165.75, 120.25, 145.50, 155.75, '2024-04-13 14:40:00', '2024-04-13 14:40:00'),
    (14, 175.50, 105.25, 58.75, 140.00, 125.25, 215.50, 135.75, 100.00, 155.75, 170.00, 125.50, 150.75, 160.00, '2024-04-14 12:45:00', '2024-04-14 12:45:00'),
    (15, 180.75, 110.00, 64.50, 145.00, 130.00, 220.75, 140.50, 105.25, 160.00, 175.25, 130.75, 155.00, 165.25, '2024-04-15 10:20:00', '2024-04-15 10:20:00');
