import sqlite3

db_path = r"C:/Users/davi emmerick/OneDrive/Área de Trabalho/Data Analytics/database.db"

def load_data (df, db_path):
    conn = sqlite3.connect(db_path)
    df.to_sql('electric_vehicles', conn, if_exists='append', index=False)
    conn.commit()
    conn.close()

