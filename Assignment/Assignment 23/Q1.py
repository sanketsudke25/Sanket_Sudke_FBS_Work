users = {
    "admin": "12345",
    "sanket": "python123"
}

def login():
    print("=== Login System ===")
    username = input("Enter username: ")
    password = input("Enter password: ")

   
    if username in users and users[username] == password:
        print(" Login successful! Welcome,", username)
    else:
        print(" Login failed! Invalid username or password.")


login()