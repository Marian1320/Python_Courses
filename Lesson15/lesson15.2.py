# Write a function that generates a random password for the user. Allow the user to specify
# the length and complexity of the password (include letters, numbers, and symbols).

import string
import random

def generate_password(length, include_letters, include_numbers, include_symbols):
    characters= ""
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    if not characters:
        raise ValueError("At least one type of character (letters, numbers, symbols) must be included.")

    password = ''.join(random.choices(characters, k=length))
    return password

password=generate_password(length=5,include_letters=True,include_numbers=True,include_symbols=True)
print(password)
