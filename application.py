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