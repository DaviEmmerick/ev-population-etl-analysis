import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect("database.db")

df = pd.read_sql_query("SELECT * FROM electric_vehicles", conn)

print(df.columns.values)
conn.close()
print("\n")

nullCounts = df.isnull().sum()
print(nullCounts)
print("\n")

# Análise dos Dados existentes  

m_counts = df["Make"].value_counts().head()
plt.figure(figsize=(12, 6))
sns.barplot(x=m_counts.index, y=m_counts.values,  hue=m_counts.index, palette="viridis", legend=False)
plt.xlabel("Marca")
plt.ylabel("Número de Veículos")
plt.title("Top 10 Marcas de Veículos Elétricos")
plt.xticks(rotation=45)
plt.show()



