# Write a simple login system where the user enters a username and password. Handle
# the KeyError by raising a custom exception if the username is not found in the users
# database(dictionary).
# Custom exception for when the username is not found
# Function to simulate login

def login_system(username, password, user_db):
    try:
        if username not in user_db:
            raise KeyError(f"Error: Username '{username}' not found in the database.")

        if user_db[username] == password:
            print("Login successful")
        else:
            print("Invalid password")

    except KeyError as e:
        print(e)


user_db = {
    "alice": "password123",
    "gor": "securepass",
    "ani": "mypassword"
}

login_system("alice", "password123", user_db)


