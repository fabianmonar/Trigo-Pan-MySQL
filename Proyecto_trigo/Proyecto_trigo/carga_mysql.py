import pandas as pd
import mysql.connector

# 1- Leer csv limpio
df = pd.read_csv('trigo_limpio.csv')
print(f"Cargando {len(df)} filas a MySQL...")

# Si te agregaste la columna decada, la sacamos para la carga
if 'decada' in df.columns:
    df = df.drop(columns=['decada'])

# 2- Conectar - PONE TU CONTRASEÑA DE WORKBENCH
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", # <- CAMBIA ESTO. Si tu Workbench entra sin pass, dejalo ""
    database="trigo_db"
)
cursor = conn.cursor()

# 3- Crear tabla en el orden EXACTO del CSV
cursor.execute("DROP TABLE IF EXISTS trigo")
cursor.execute("""
CREATE TABLE trigo (
    cultivo VARCHAR(100),
    anio INT,
    campania VARCHAR(20),
    provincia VARCHAR(100),
    provincia_id INT,
    departamento VARCHAR(100),
    departamento_id INT,
    superficie_sembrada_ha FLOAT,
    superficie_cosechada_ha FLOAT,
    produccion_tm FLOAT,
    rendimiento_kgxha FLOAT,
    rendimiento_tn_ha FLOAT,
    pct_perdida FLOAT,
    superficie_cosechada FLOAT
)
""")
# Tip: si te da error por la cantidad de columnas, usa esta forma segura:

# Definimos el orden exacto que vamos a insertar
columnas = ['cultivo','anio','campania','provincia','provincia_id','departamento','departamento_id','superficie_sembrada_ha','superficie_cosechada_ha','produccion_tm','rendimiento_kgxha','rendimiento_tn_ha','pct_perdida','superficie_cosechada']

# Creamos una copia solo con esas columnas (las que existan)
columnas_existentes = [c for c in columnas if c in df.columns]
df_carga = df[columnas_existentes]

# 4- Insertar - mucho mas rapido
placeholders = ", ".join(["%s"] * len(columnas_existentes))
sql = f"INSERT INTO trigo ({', '.join(columnas_existentes)}) VALUES ({placeholders})"

for _, row in df_carga.iterrows():
    cursor.execute(sql, tuple(row))

conn.commit()
print(f"Listo! {len(df_carga)} filas cargadas en trigo_db.trigo")
conn.close()