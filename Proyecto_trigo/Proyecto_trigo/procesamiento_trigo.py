import pandas as pd
import numpy as np
from conexion import get_conexion

# 1. CARGAR DE MYSQL
con = get_conexion()
df = pd.read_sql("SELECT * FROM trigo", con)
con.close()

# Convertir fecha para poder filtrar por año
df['fecha_siembra'] = pd.to_datetime(df['fecha_siembra'])
df['anio'] = df['fecha_siembra'].dt.year

print("✓ Datos cargados")
print(df.head())
print(df.columns.tolist())

# 2. FILTROS Y GROUPBY
print("\n--- FILTRO 1: Alta producción > 110 toneladas ---")
filtro1 = df[df['toneladas'] > 110]
print(filtro1)

print("\n--- FILTRO 2: Solo variedad Klein Favorito ---")
filtro2 = df[df['variedad'] == 'Klein Favorito']
print(filtro2)

print("\n--- GROUPBY 1: Total toneladas por variedad ---")
prod_variedad = df.groupby('variedad')['toneladas'].sum().reset_index().sort_values(by='toneladas', ascending=False)
print(prod_variedad)

print("\n--- GROUPBY 2: Promedio rendimiento por lote ---")
rend_lote = df.groupby('lote')['rendimiento'].mean().reset_index()
print(rend_lote)

# 3. DESCRIBE
print("\n--- DESCRIBE ---")
print(df[['toneladas','rendimiento']].describe())
print("""
INTERPRETACIÓN:
- El promedio de toneladas es ~108 tn, con un desvío chico.
- El rendimiento promedio es ~30 qq/ha, max 32.5 indica buen rinde en Lote Norte.
""")

# 4. NUMPY
print("\n--- NUMPY ---")
promedio_tn = np.mean(df['toneladas'])
mediana_rend = np.median(df['rendimiento'])
std_tn = np.std(df['toneladas'])
df['toneladas_proyectadas'] = np.multiply(df['toneladas'], 1.15) # Proyección +15%

print(f"Promedio toneladas (numpy): {promedio_tn:.2f}")
print(f"Mediana rendimiento (numpy): {mediana_rend}")
print(f"Desvío estándar toneladas: {std_tn:.2f}")
print(df[['toneladas','toneladas_proyectadas']].head())

# 5. 5 PREGUNTAS
print("\n--- 5 PREGUNTAS ---")
print(f"P1: Variedad con más toneladas totales: {prod_variedad.iloc[0]['variedad']}")
print(f"P2: Lote más rendidor: {rend_lote.sort_values('rendimiento', ascending=False).iloc[0]['lote']}")
print(f"P3: Campaña con mayor producción: {df.groupby('campana')['toneladas'].sum().idxmax()}")
print(f"P4: Rendimiento promedio general: {promedio_tn}")
print(f"P5: Correlación toneladas vs rendimiento: {np.corrcoef(df['toneladas'], df['rendimiento'])[0,1]:.2f}")