import sqlite3

db_path = "../data/database.db"

def load_data (df, db_path):
    conn = sqlite3.connect(db_path)
    df.to_sql('electric_vehicles', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()

