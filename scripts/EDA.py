import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carpeta raíz del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
input_file = os.path.join(BASE_DIR, "data", "Base.xlsx") #data/Base.xlsx
output_dir = os.path.join(BASE_DIR, "out") #out
os.makedirs(output_dir, exist_ok=True)

# 1. Cargar datos
df = pd.read_excel(input_file)

###

# Conteo y porcentaje de valores faltantes
conteo_faltante = df.isnull().sum()
faltante_porcentaje = df.isnull().mean() * 100

# Guardar resumen en CSV
resumen_faltantes=pd.DataFrame({
    "nombres": df.columns,
    "conteo_faltantes": df.isnull().sum().values,
    "porcentaje_faltantes": df.isnull().mean().values * 100
})
resumen_faltantes.to_csv(os.path.join(output_dir, "missingness.csv"), index=False)

# Visualización de columnas con faltantes
plt.figure(figsize=(10,6))
conteo_faltante[conteo_faltante > 0].sort_values().plot.barh(color="salmon")
plt.title("Valores faltantes por columna")
plt.xlabel("Número de valores faltantes")
plt.tight_layout()

# Guardar figura
plt.savefig(os.path.join(output_dir, "resumen_faltantes.png"))
plt.close()

###

# 2. Información general
print(df.info())
print(df.describe())

# 3. Columnas numéricas
columnas_numericas = df.select_dtypes(include=["int64", "float64"]).columns

# 4. Histogramas para variables continuas 
for col in df.select_dtypes(include=["float64"]).columns:
    plt.figure(figsize=(8,6))
    df[col].hist(bins=20)
    plt.title(f"Histograma de {col}")
    plt.xlabel(col)
    plt.ylabel("Frecuencia")
    plt.savefig(os.path.join(output_dir, f"{col}_hist.png"))
    plt.close()

# 5. Distribuciones generales (boxplots para todas las numéricas)
for col in columnas_numericas:
    plt.figure(figsize=(8,6))
    sns.boxplot(x=df[col])
    plt.title(f"Distribución de {col}")
    plt.savefig(os.path.join(output_dir, f"{col}_boxplot.png"))
    plt.close()