import sqlite3
import pandas as pd
from datetime import datetime

def process_and_update_data(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("UPDATE eletric_vehicles SET County = 'Desconhecido' WHERE County IS NULL")
    cursor.execute('UPDATE eletric_vehicles SET [Legislative District] = "Desconhecido" WHERE [Legislative District] IS NULL')
    conn.commit()

    df = pd.read_sql_query("SELECT * FROM eletric_vehicles", conn)
    conn.close()

    if "Postal Code" in df.columns:
        df["Postal Code"] = df["Postal Code"].astype(str)

    df["Missing_Count"] = df.isnull().sum(axis=1)

    state_counts = df.groupby('City').size().reset_index(name='Vehicle_Count')

    current_year = datetime.now().year
    df["Vehicle_Age"] = current_year - df["Model Year"]

    age_by_city = df.groupby("City")["Vehicle_Age"].mean().round(2).reset_index(name="Avg_Vehicle_Age")

    conn = sqlite3.connect(db_path)
    df.to_sql('eletric_vehicles', conn, if_exists='replace', index=False)
    conn.close()