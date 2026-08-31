import pandas as pd
import mysql.connector

# 1- Leer csv limpio
df = pd.read_csv('trigo_limpio.csv')
print(f"Cargando {len(df)} filas a MySQL...")

# 2- Conectar
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="trigo_db"
)
cursor = conn.cursor()

# 3- Crear tabla
cursor.execute("DROP TABLE IF EXISTS trigo")
cursor.execute("""
CREATE TABLE trigo (
    cultivo VARCHAR(50),
    anio INT,
    campania VARCHAR(20),
    provincia VARCHAR(100),
    provincia_id FLOAT,
    departamento VARCHAR(100),
    departamento_id FLOAT,
    superficie_sembrada_ha INT,
    superficie_cosechada_ha INT,
    produccion_tm INT,
    rendimiento_kgxha INT,
    rendimiento_tn_ha FLOAT,
    pct_perdida FLOAT
)
""")

# 4- Insertar
for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO trigo VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()
print(f"Listo! {cursor.rowcount} filas cargadas")
conn.close()