import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_visualizations(db_path="database.db"):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM eletric_vehicles", conn)

    m_counts = df["Make"].value_counts().head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(x=m_counts.index, y=m_counts.values, palette="viridis", legend=False)
    plt.xlabel("Marca")
    plt.ylabel("Número de Veículos")
    plt.title("Top 10 Marcas de Veículos Elétricos")
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.histplot(df['Vehicle_Age'], kde=True, color="blue")
    plt.title("Distribuição da Idade dos Veículos Elétricos")
    plt.xlabel("Idade do Veículo")
    plt.ylabel("Frequência")
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.scatterplot(x="Base MSRP", y="Electric Range", data=df, color="purple")
    plt.title("Preço Base vs Alcance Elétrico")
    plt.xlabel("Preço Base (MSRP)")
    plt.ylabel("Alcance Elétrico (em milhas)")
    plt.show()

    conn.close()