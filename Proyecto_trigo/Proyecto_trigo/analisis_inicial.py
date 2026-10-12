import pandas as pd
import numpy as np

# 1. Cargar archivos
estimaciones = pd.read_csv("estimaciones-agricolas-2026-03.csv")
serie_trigo = pd.read_csv("serie-de-tiempo-trigo.csv")

# Limpieza de nombres de columnas
estimaciones.columns = estimaciones.columns.str.strip().str.lower()

# 2. Exploración (CAPTURA 1 y 2)
print("=== ESTIMACIONES AGRÍCOLAS ===")
print(estimaciones.info())
print("\nColumnas detectadas:", estimaciones.columns.tolist())
print("\nNulos:", estimaciones.isnull().sum().sum(), "| Duplicados:", estimaciones.duplicated().sum())

# 3. Filtrado por cultivo
trigo_df = estimaciones[estimaciones['cultivo'].str.contains('trigo', case=False, na=False)].copy()
print(f"\nFilas de trigo encontradas: {len(trigo_df)}")

# 4. Limpieza
trigo_df = trigo_df.drop_duplicates()

# NOMBRES REALES DEL CSV
col_sembrada = 'superficie_sembrada_ha'
col_cosechada = 'superficie_cosechada_ha'
col_produccion = 'produccion_tm'
col_rendimiento_original = 'rendimiento_kgxha'
col_anio = 'anio'

columnas_numericas = [col_sembrada, col_cosechada, col_produccion, col_rendimiento_original, col_anio]

for col in columnas_numericas:
    if col in trigo_df.columns:
        trigo_df[col] = pd.to_numeric(trigo_df[col], errors='coerce').fillna(0)

# 5. Cálculo de las 5 variables que pide el DER corregido (CAPTURA 3)
trigo_df['superficie_cosechada'] = trigo_df[col_cosechada]

trigo_df['rendimiento_kgxha'] = trigo_df[col_rendimiento_original]

trigo_df['rendimiento_tn_ha'] = np.where(
    trigo_df[col_cosechada] > 0,
    trigo_df[col_produccion] / trigo_df[col_cosechada],
    0
)

trigo_df['pct_perdida'] = np.where(
    trigo_df[col_sembrada] > 0,
    ((trigo_df[col_sembrada] - trigo_df[col_cosechada]) / trigo_df[col_sembrada]) * 100,
    0
)

trigo_df['campania'] = trigo_df[col_anio].astype(int).astype(str) + "/" + (trigo_df[col_anio].astype(int)+1).astype(str)

print("\n=== 5 Columnas nuevas validadas ===")
print(trigo_df[['superficie_cosechada','rendimiento_kgxha','rendimiento_tn_ha','pct_perdida','campania']].head())
print(trigo_df[['superficie_cosechada','rendimiento_kgxha','rendimiento_tn_ha','pct_perdida','campania']].describe())

# 6. Exportación
trigo_df.to_csv("trigo_limpio.csv", index=False)
print(f"\n¡LISTO! Archivo 'trigo_limpio.csv' generado con {len(trigo_df)} filas.")

# 7. 5 PREGUNTAS DEL INFORME ISPC
print("\n=== RESPUESTAS INFORME ===")

# 1- Promedio ha sembradas
promedio = trigo_df[col_sembrada].mean()
print(f"1) Promedio sembrado: {promedio:.2f} ha")

# 2- Volumen total últimas 50 campañas
ultimo_anio = int(trigo_df[col_anio].max())
total_50 = trigo_df[trigo_df[col_anio] >= ultimo_anio-50][col_produccion].sum()
print(f"2) Total últimas 50 campañas ({ultimo_anio-50}-{ultimo_anio}): {total_50:,.0f} tn")

# 3- Año max rendimiento
max_ren = trigo_df.loc[trigo_df['rendimiento_kgxha'].idxmax()]
print(f"3) Max rendimiento: {max_ren['rendimiento_kgxha']} kg/ha en {int(max_ren[col_anio])}")

# 4- Volumen mínimo y año
prod_por_anio = trigo_df.groupby(col_anio)[col_produccion].sum()
anio_min = int(prod_por_anio.idxmin())
print(f"4) Min producción: {prod_por_anio.min():,.0f} tn en {anio_min}")

# 5- % pérdida por década
trigo_df['decada'] = (trigo_df[col_anio]//10*10).astype(int).astype(str) + "s"
perdida_decada = trigo_df.groupby('decada')['pct_perdida'].mean().round(2)
print("\n5) % Pérdida promedio por década:")
print(perdida_decada)