# Happens once
password = input("Enter password: ")

# Will keep happening as long as the user input is NOT pass123
while password != "pass123":
    password = input("Enter password: ")

# Will print and the while loop stops when the user input IS pass123
print("Password correct")
