import pandas as pd

def migrate_datasets_metadata(conn):
    datasets = pd.read_csv("DATA/datasets_metadata.csv")
    datasets.to_sql("datasets_metadata", conn, if_exists="append", index=False)

def get_all_datasets_metadata(conn):
    query = "SELECT * FROM datasets_metadata"
    datasets_table = pd.read_sql_query(query, conn)
    conn.commit()
    return datasets_table