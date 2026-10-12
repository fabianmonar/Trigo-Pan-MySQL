DROP DATABASE IF EXISTS trigo_db;
CREATE DATABASE trigo_db;
USE trigo_db;

CREATE TABLE trigo (
    id INT PRIMARY KEY AUTO_INCREMENT,
    campana VARCHAR(20),
    variedad VARCHAR(100),
    lote VARCHAR(100),
    toneladas DECIMAL(10,2),
    rendimiento DECIMAL(10,2),
    fecha_siembra DATE
);

INSERT INTO trigo (campana, variedad, lote, toneladas, rendimiento, fecha_siembra) VALUES
('2023/24', 'Klein Favorito', 'Lote Norte', 120.50, 32.5, '2023-06-15'),
('2024/25', 'ACA 360', 'Lote Sur', 95.20, 28.7, '2024-06-10'),
('2024/25', 'Klein Favorito', 'Lote Norte', 110.00, 30.1, '2024-06-12');

SELECT * FROM trigo;