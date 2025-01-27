# Write a program to check if two strings are balanced. For example, strings s1 and
# s2 are balanced if all the characters in the s1 are present in s2. The character’s
# position doesn’t matter.

s1 = "Yn"
s2 = "PYnative"

exists = True

for char in s2:
    if char not in s1:
        exists = False
        break

if exists:
    print("True")
else:
    print("False")
