import os
import pandas as pd
import minsearch

DATA_PATH = os.getenv("DATA_PATH", "../data/clean_data.csv")

def load_index(data_path=DATA_PATH):

    df = pd.read_csv(data_path)
    df.columns = df.columns.str.lower()
    df = df.dropna(subset=['primarytype'])

    documents = df.to_dict(orient='records')

    index = minsearch.Index(
        text_fields=['primarytype','reviews'],
        keyword_fields=['id']
    )

    index.fit(documents)

    return index