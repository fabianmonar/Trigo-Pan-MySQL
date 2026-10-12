USE trigo_db;

-- 1. Total de registros
SELECT COUNT(*) as total_filas FROM trigo;

-- 2. Produccion total por provincia (Top 5)
SELECT provincia, SUM(produccion) / 1000 as produccion_miles_tn
FROM trigo
GROUP BY provincia
ORDER BY produccion_miles_tn DESC
LIMIT 5;

-- 3. Rinde promedio por decada
SELECT FLOOR(anio/10)*10 as decada, ROUND(AVG(rinde), 2) as rinde_promedio_kg_ha
FROM trigo
GROUP BY decada
ORDER BY decada;

-- 4. Superficie sembrada vs cosechada por campania
SELECT campania, SUM(superficie_sembrada) as sembrada, SUM(superficie_cosechada) as cosechada
FROM trigo
GROUP BY campania
ORDER BY campania DESC
LIMIT 10;

-- 5. Anios con mayor produccion de trigo candeal
SELECT anio, SUM(produccion) as total
FROM trigo
WHERE cultivo LIKE '%candeal%'
GROUP BY anio
ORDER BY total DESC
LIMIT 10;