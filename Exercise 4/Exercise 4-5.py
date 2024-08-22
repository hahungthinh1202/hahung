username = "python"
password = "rules"
attempt = 1
while True:
    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")
    if input_username == username and input_password == password:
        print("Access granted")
        break
    elif attempt < 5:
        print("Invalid username or password, please try again!")
        attempt += 1
    else:
        print("Access denied")
        break
