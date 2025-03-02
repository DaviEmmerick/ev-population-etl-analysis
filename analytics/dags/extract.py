import pandas as pd

def extract_data(file_path):
    df = pd.read_csv(file_path)
    return df

file_path = "../data/Electric_Vehicle_Population_Data.csv"
df = extract_data(file_path)
