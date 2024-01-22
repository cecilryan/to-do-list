#Functions

def Intro(user, game):
    print("Welcome, " + user + "! Are you ready to play " + game + "?")

def check_credentials():
    # Hardcoded valid username and password (modify these)
    valid_username = "tempusername"
    valid_password = "TempPassword"


    # Get user input for username and password
    username = input("Enter username: ")
    password = input("Enter password: ")


    # Convert the entered username to lowercase for case-insensitive comparison
    username = username.lower()
    # Check if the entered username and password match the valid credentials
    if (username == valid_username) and (password == valid_password):
        print("Access Granted")
    if (username != valid_username) or (password != valid_password):
        print("Access Denied")

def outro(user, game): 
    print("Thanks for playing " + game + ", " + user + "! Goodbye!")

