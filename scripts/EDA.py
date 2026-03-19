import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
import io

#Argumentos desde terminal 
parser = argparse.ArgumentParser(description="EDA Script")
parser.add_argument("-i", "--input", required=True, help="Ruta del archivo de entrada (CSV/Excel)")
parser.add_argument("-o", "--output", required=True, help="Carpeta de salida")
args = parser.parse_args()

input_file = args.input
output_dir = args.output
os.makedirs(output_dir, exist_ok=True)

#Cargar datos
if input_file.endswith(".csv"):
    df = pd.read_csv(input_file)
else:
    df = pd.read_excel(input_file)

#Crear objeto PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "Reporte EDA", ln=True, align="C")
pdf.ln(10)

# df.info()
buffer = io.StringIO()
df.info(buf=buffer)
info_text = buffer.getvalue()
buffer.close()

pdf.set_font("Arial", size=10)
pdf.multi_cell(0, 5, f"Información general:\n{info_text}")

# df.describe()
pdf.ln(10)
pdf.cell(0, 10, "Estadísticas descriptivas:", ln=True)
desc = df.describe().round(2)
pdf.set_font("Arial", size=8)
for col in desc.columns:
    pdf.cell(0, 10, f"{col}: {desc[col].to_dict()}", ln=True)

#Missingness 
conteo_faltante = df.isnull().sum()
plt.figure(figsize=(10,6))
conteo_faltante[conteo_faltante > 0].sort_values().plot.barh(color="salmon")
plt.title("Valores faltantes por columna")
plt.xlabel("Número de valores faltantes")
plt.tight_layout()
missingness_path = os.path.join(output_dir, "missingness.png")
plt.savefig(missingness_path)
plt.close()

pdf.add_page()
pdf.cell(0, 10, "Valores faltantes:", ln=True)
pdf.image(missingness_path, x=10, y=30, w=180)
os.remove(missingness_path) ### aqui borramos las imagenes como se van usando jsjsjs


#Histogramas
for col in df.select_dtypes(include=["float64"]).columns:
    plt.figure(figsize=(8,6))
    df[col].hist(bins=20)
    plt.title(f"Histograma de {col}")
    plt.xlabel(col)
    plt.ylabel("Frecuencia")
    hist_path = os.path.join(output_dir, f"{col}_hist.png")
    plt.savefig(hist_path)
    plt.close()

    pdf.add_page()
    pdf.cell(0, 10, f"Histograma de {col}", ln=True)
    pdf.image(hist_path, x=10, y=30, w=180)
    os.remove(hist_path) ### aqui borramos las imagenes como se van usando jsjsjs

#Boxplots y outliers
for col in df.select_dtypes(include=["int64", "float64"]).columns:
    plt.figure(figsize=(8,6))
    sns.boxplot(x=df[col])
    plt.title(f"Distribución de {col}")
    box_path = os.path.join(output_dir, f"{col}_boxplot.png")
    plt.savefig(box_path)
    plt.close()

    pdf.add_page()
    pdf.cell(0, 10, f"Boxplot de {col}", ln=True)
    pdf.image(box_path, x=10, y=30, w=180)
    os.remove(box_path)  ### aqui borramos las imagenes como se van usando jsjsjs

#Correlaciones
pdf.add_page()
pdf.cell(0, 10, "Correlations: Matriz de correlación entre variables numéricas", ln=True)

#Matriz de correlación
corr = df.corr(numeric_only=True)

# Graficar heatmap
plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de correlación")
corr_path = os.path.join(output_dir, "correlation_matrix.png")
plt.savefig(corr_path)
plt.close()

pdf.image(corr_path, x=10, y=30, w=180)
os.remove(corr_path)



pdf_output = os.path.join(output_dir, "EDA_reporte.pdf")
pdf.output(pdf_output)