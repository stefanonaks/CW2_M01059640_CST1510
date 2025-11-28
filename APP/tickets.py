import pandas as pd
from APP.db import conn

def migrate_it_tickets():
    tickets = pd.read_csv("DATA/it_tickets.csv")
    tickets.to_sql("it_tickets", conn, if_exists="append", index=False)

def get_all_it_tickets():
    query = "SELECT * FROM it_tickets"
    tickets_table = pd.read_sql_query(query, conn)
    conn.close()
    return tickets_table