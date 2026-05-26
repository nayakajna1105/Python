print(" Login System")

# correct details
correct_username = "admin"
correct_password = "123"

# user input
username = input("Enter username: ")
password = input("Enter password: ")

# checking
if username == correct_username and password == correct_password:
    print("Login successful!")
    print("Welcome", username)
else:
    print("Wrong username or password")
    print("Access denied")

print("Program ended")
