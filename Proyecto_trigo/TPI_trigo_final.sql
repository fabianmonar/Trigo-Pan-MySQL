USE trigo_db;

-- 1. Cantidad total
SELECT COUNT(*) AS total_registros, COUNT(DISTINCT campania) AS total_campanias FROM trigo;

-- 2. Producción por provincia
SELECT provincia, SUM(produccion_tm)/1000 AS miles_tn FROM trigo GROUP BY provincia ORDER BY miles_tn DESC LIMIT 5;

-- 3. Rinde por década
SELECT FLOOR(anio/10)*10 AS decada, ROUND(AVG(rendimiento_kgxha),2) AS rinde_promedio FROM trigo GROUP BY decada ORDER BY decada;

-- 4. Evolución anual
SELECT anio, SUM(produccion_tm) AS total_tn FROM trigo GROUP BY anio ORDER BY anio DESC LIMIT 10;