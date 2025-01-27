#Count all letters, digits, and special symbols from a given string
word = "P@#yn26at^&i5ve"

low_case = 0
upper_case = 0
digit = 0
symbol = 0

for char in word:
    if char.islower():
        low_case += 1
    elif char.isupper():
        upper_case += 1
    elif char.isdigit():
        digit += 1
    else:
        symbol += 1

char = low_case + upper_case

print("Letters:", char)
print("Digits:", digit)
print("Symbols:", symbol)
