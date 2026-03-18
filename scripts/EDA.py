# eda.py
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar datos
df = pd.read_excel("data/Base.xlsx")

# 2. Información general
print(df.info())
print(df.describe())




