import pandas as pd

df = pd.read_csv('../data/clean_data.csv')
df.columns = df.columns.str.lower()
df = df.dropna(subset=['primarytype'])

documents = df.to_dict(orient='records')
