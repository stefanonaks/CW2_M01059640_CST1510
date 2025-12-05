import pandas as pd

def migrate_it_tickets(conn):
    tickets = pd.read_csv("DATA/it_tickets.csv")
    tickets.to_sql("it_tickets", conn, if_exists="append", index=False)

def get_all_it_tickets(conn):
    query = "SELECT * FROM it_tickets"
    tickets_table = pd.read_sql_query(query, conn)
    conn.commit()
    return tickets_table