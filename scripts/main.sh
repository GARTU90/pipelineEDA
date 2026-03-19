INPUT_FILE=$1   # primer argumento: archivo de entrada
OUTPUT_DIR=$2   # segundo argumento: carpeta de salida

# Ejecutar el script de Python con los argumentos
python3 scripts/eda.py -i "$INPUT_FILE" -o "$OUTPUT_DIR"