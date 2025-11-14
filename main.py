from application import register_user, login_user

def menu():
    print("---Choose an option---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

def main():
    while True:
        menu()
        choice = int(input("Enter choice: "))
        if choice == 1:
            register_user()
        elif choice == 2:
            login_user()
        elif choice == 3:
            print("See you next time.")
            break

main()
