# Write a Python program to find if a given string starts with a given
# character using Lambda.

starts_with_char = lambda string, char: string.startswith(char)

input_string = "Hello, world!"
given_char = 'H'

if starts_with_char(input_string, given_char):
    print(given_char)
else:
    print('error')