# Write a Python program that asks the user to enter a password.
# Keep asking for the password until the correct password "secret" is entered.
# Provide appropriate feedback to the user.

x=input("your password: ")

while x!='secret':
    print("try again")
    x=input("your password: ")

print("ok")
