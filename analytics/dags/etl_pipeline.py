from dags.extract import extract_data
from dags.load import load_data

file_path = "../data/Electric_Vehicle_Population_Data.csv"

df = extract_data(file_path)

load_data(df, 'database.db')
