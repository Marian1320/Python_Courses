# Write a Python program to check whether a given string is number or
# not using Lambda.

x=input()
is_number=lambda x: x.isdigit()
if is_number(x):
    print("True")
else:
    print("False")