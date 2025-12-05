import pandas as pd
from APP.db import conn

def migrate_cyber_incidents():
    cyber = pd.read_csv("DATA/cyber_incidents.csv")
    cyber.to_sql("cyber_incidents", conn, if_exists="append", index=False)

def get_all_cyber_incidents():
    query = "SELECT * FROM cyber_incidents"
    cyber_table = pd.read_sql_query(query, conn)
    conn.commit()
    return cyber_table