import pandas as pd
import numpy as np

# 1. Cargar archivos
estimaciones = pd.read_csv("estimaciones-agricolas-2026-03.csv")
serie_trigo = pd.read_csv("serie-de-tiempo-trigo.csv")

estimaciones.columns = estimaciones.columns.str.strip().str.lower()

# 2. Exploración
print("=== ESTIMACIONES AGRÍCOLAS ===")
print(estimaciones.info())
print("\nColumnas detectadas:", estimaciones.columns.tolist())

# 3. Filtrado por cultivo
trigo_df = estimaciones[estimaciones['cultivo'].str.contains('trigo', case=False, na=False)].copy()
print(f"\nFilas de trigo encontradas: {len(trigo_df)}")

# 4. Limpieza
trigo_df = trigo_df.drop_duplicates()

# NOMBRES REALES DE TU CSV (corregidos)
col_sembrada = 'superficie_sembrada_ha'
col_cosechada = 'superficie_cosechada_ha'
col_produccion = 'produccion_tm' # <- ESTE ERA EL ERROR, AHORA ES EL NOMBRE REAL
col_rendimiento_original = 'rendimiento_kgxha'

columnas_numericas = [col_sembrada, col_cosechada, col_produccion, col_rendimiento_original]

for col in columnas_numericas:
    trigo_df[col] = pd.to_numeric(trigo_df[col], errors='coerce').fillna(0)

# 5. Cálculo de variables
# Rendimiento en Tn/Ha
trigo_df['rendimiento_tn_ha'] = np.where(
    trigo_df[col_cosechada] > 0,
    trigo_df[col_produccion] / trigo_df[col_cosechada],
    0
)

# Porcentaje de pérdida
trigo_df['pct_perdida'] = np.where(
    trigo_df[col_sembrada] > 0,
    ((trigo_df[col_sembrada] - trigo_df[col_cosechada]) / trigo_df[col_sembrada]) * 100,
    0
)

print(trigo_df[[col_sembrada, col_cosechada, col_produccion, 'rendimiento_tn_ha', 'pct_perdida']].head())

# 6. Exportación
trigo_df.to_csv("trigo_limpio.csv", index=False)
print(f"\n¡LISTO! Archivo 'trigo_limpio.csv' generado con {len(trigo_df)} filas.")

# 5 PREGUNTAS DEL INFORME ISPC
print("\n=== RESPUESTAS ===")

# 1- Promedio ha sembradas
promedio = trigo_df['superficie_sembrada_ha'].mean()
print(f"1) Promedio sembrado: {promedio:.2f} ha")

# 2- Volumen total últimas 50 campañas
ultimo_anio = trigo_df['anio'].max()
total_50 = trigo_df[trigo_df['anio'] >= ultimo_anio-50]['produccion_tm'].sum()
print(f"2) Total últimas 50 campañas: {total_50:,} tn")

# 3- Año max rendimiento
max_ren = trigo_df.loc[trigo_df['rendimiento_kgxha'].idxmax()]
print(f"3) Max rendimiento: {max_ren['rendimiento_kgxha']} kg/ha en {max_ren['anio']}")

# 4- Volumen mínimo y año
prod_por_anio = trigo_df.groupby('anio')['produccion_tm'].sum()
anio_min = prod_por_anio.idxmin()
print(f"4) Min producción: {prod_por_anio.min():,} tn en {anio_min}")

# 5- % pérdida por década
trigo_df['decada'] = (trigo_df['anio']//10*10).astype(str) + "s"
perdida_decada = trigo_df.groupby('decada')['pct_perdida'].mean()
print("\n5) % Pérdida promedio por década:")
print(perdida_decada)