# Exploración Inicial de Datos – Registro Nacional de Cáncer

## Descripción
Este proyecto implementa un pipeline reproducible para realizar un análisis exploratorio de datos (EDA) sobre `Base.xlsx` del Registro Nacional de Cáncer.

## Autor
Juan Daniel Rangel Avila
Contacto: juan.daniel.rangel.avila@gmail.com

## Requisitos
- Python 3.13.2
- Librerías: ver `requirements.txt`

## Estructura del repositorio
- `scripts/` → incluye `eda.py` con la lógica del análisis.
- `out/` → resultados y reporte final (`Reporte.pdf`).
- `main.sh` → script para ejecutar el pipeline completo.
- `README.md` → documentación técnica.
- `.gitignore` → excluye la carpeta `data/`.

## Uso
1. Crear entorno virtual: `python -m venv .venv`
2. Activar entorno: `.venv\Scripts\activate`
3. Instalar dependencias: `pip install -r requirements.txt`
4. Ejecutar pipeline: `bash scripts/main.sh data/Base.xlsx out/`

## Licencia
GNU GPL v3

## Referencias
- [Pandas Documentation](https://pandas.pydata.org/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [FPDF Documentation](http://www.fpdf.org/)
- [openpyxl Documentation](https://openpyxl.readthedocs.io/en/stable/)
- [Seaborn Documentation](https://seaborn.pydata.org/)
