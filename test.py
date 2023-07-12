import os

def register_user():
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as default_file:
            default_file.write("admin;password")

    with open("user.txt", 'r') as user_file:
        user_data = user_file.read().split("\n")

    username_password = {}
    for user in user_data:
        if user:
            username, password = user.split(';')
            username_password[username] = password

    while True:
        new_username = input("New Username: ")
        if new_username in username_password:
            print("This username already exists. Please choose a different username.")
        else:
            password = input("Password: ")
            with open("user.txt", "a") as user_file:
                user_file.write(f"{new_username};{password}\n")
            print("Username successfully registered.")
            break
