import sqlite3
import pandas as pd

conn = sqlite3.connect("DATA/intelligence.db")

def create_table():
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL
    )""")
    conn.commit()

def add_user(conn, username, hash):
    cursor = conn.cursor()
    sql = ("""INSERT INTO users
            (username, password_hash)
            VALUES (?, ?)""")
    parameters = (username, hash)
    cursor.execute(sql, parameters)
    print(f"Added user: {username}")
    conn.commit()

def get_users():
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM users""")
    all_users = cursor.fetchall()
    conn.close()
    return all_users

def migrate_user_data():
    with open("DATA/users.txt") as f:
        users = f.readlines() 
    for user in users:
        name, hash = user.strip().split(":")
        add_user(conn, name, hash)
    conn.close()

def delete_user_data():
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM users WHERE username = ?""", ("testuser",))
    conn.commit()
    print(f"Deleted {cursor.rowcount} user(s).")

def migrate_cyber_incidents():
    cyber = pd.read_csv("DATA/cyber_incidents.csv")
    cyber.to_sql("cyber_incidents", conn, if_exists="append", index=False)

def migrate_datasets_metadata():
    datasets = pd.read_csv("DATA/datasets_metadata.csv")
    datasets.to_sql("datasets_metadata", conn, if_exists="append", index=False)

def migrate_it_tickets():
    tickets = pd.read_csv("DATA/it_tickets.csv")
    tickets.to_sql("it_tickets", conn, if_exists="append", index=False)

query = "SELECT * FROM cyber_incidents"
cyber_table = pd.read_sql_query(query, conn)
print(cyber_table.head())