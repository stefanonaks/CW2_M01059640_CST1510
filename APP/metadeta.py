import pandas as pd
from APP.db import conn

def migrate_datasets_metadata():
    datasets = pd.read_csv("DATA/datasets_metadata.csv")
    datasets.to_sql("datasets_metadata", conn, if_exists="append", index=False)

def get_all_datasets_metadata():
    query = "SELECT * FROM datasets_metadata"
    datasets_table = pd.read_sql_query(query, conn)
    conn.commit()
    return datasets_table