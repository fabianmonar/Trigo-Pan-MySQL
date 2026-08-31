# 🌾 TPI - Gestión de Trigo Pan | ISPC Ciencia de Datos

Sistema de gestión y registro de campañas agrícolas enfocado en la producción de Trigo Pan en Argentina.

### 📊 Dataset
Serie de Tiempo de Trigo Pan - Ministerio de Economía - Secretaría de Agricultura, Ganadería y Pesca.
Fuente: https://datos.magyp.gob.ar/dataset/estimaciones-agricolas/archivo/ca5e31b5-a51f-4738-bae0-773838b5dd1e

### ❓ Problemática
La producción de trigo es un pilar del agro argentino pero está expuesta a incertidumbre climática y económica. La falta de una herramienta que procese datos históricos impide monitorear la pérdida de superficie y el riesgo de desabastecimiento.

### 🔍 Preguntas de Análisis Resueltas
1. Promedio de hectáreas sembradas
2. Volumen total acumulado (ton) últimas 50 campañas
3. Campaña con máximo rendimiento por hectárea
4. Volumen mínimo de producción y año
5. % promedio de superficie no cosechada por década

### 🛠️ Stack Tecnológico
- MySQL Workbench - Modelado y consultas
- Python (Pandas) - Limpieza y carga de datos
- Matplotlib - Visualización (`perdida_por_decada.png`)

### 📁 Estructura
- `Trigo_DB.mwb` -> Modelo ER
- `TPI_trigo_final.sql` -> Consultas finales
- `trigo_limpio.csv` -> Dataset limpio
- `grafico_perdida.py` -> Código del gráfico

### ✅ Estado
Base de datos `trigo_db` conectada y funcional con +15k registros.
