import sqlite3
from APP.db import get_connection

conn = get_connection()

def add_user(conn, username, hash):
    cursor = conn.cursor()
    sql = ("""INSERT INTO users
            (username, password_hash)
            VALUES (?, ?)""")
    parameters = (username, hash)
    cursor.execute(sql, parameters)
    print(f"Added user: {username}")
    conn.commit()

def get_user(conn, username):
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM users WHERE username = ?""", (username,))
    user = cursor.fetchone()
    return user

def get_users(conn):
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM users""")
    all_users = cursor.fetchall()
    conn.commit()
    return all_users

def migrate_user_data(conn):
    with open("DATA/users.txt") as f:
        users = f.readlines() 
    for user in users:
        name, hash = user.strip().split(":")
        add_user(conn, name, hash)
    conn.close()

def delete_user_data(conn):
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM users WHERE username = ?""", ("testuser",))
    conn.commit()
    print(f"Deleted {cursor.rowcount} user(s).")


import bcrypt 

def hash_password(user_password):
    password_bytes = user_password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password.decode('utf-8')

def validate_password(user_password, hashed_password):
    password_bytes = user_password.encode('utf-8')
    if isinstance(hashed_password, str):
        hashed_bytes = hashed_password.encode('utf-8')
    else:
        hashed_bytes = hashed_password
    return bcrypt.checkpw(password_bytes, hashed_bytes)

def register_user():
    username = input("Enter username: ")
    user_password = input("Enter password: ")
    hashed_password = hash_password(user_password)
    with open('users.txt', 'a') as f:
        f.write(f"{username}:{hashed_password}\n")
    print("User registered successfully.")
    
def login_user():
    username = input("Enter username: ")
    user_password = input("Enter password: ")

    with open('users.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            username, hashed_password = line.strip().split(":", 1)
            if username == username:
                return validate_password(user_password, hashed_password)
    return False