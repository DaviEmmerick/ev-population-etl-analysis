from dags.extract import extract_data
from dags.load import load_data
from dags.analysis import generate_visualizations
from dags.transform import process_and_update_data
import os 

file_path = "../data/Electric_Vehicle_Population_Data.csv"
db_path = "../../database.db"

if os.path.exists(file_path):
    print("O arquivo foi encontrado!")
else:
    print("Arquivo não encontrado. Caminho incorreto.")

df = extract_data(file_path)

load_data(df, db_path)
generate_visualizations(db_path=db_path)
process_and_update_data(db_path=db_path)