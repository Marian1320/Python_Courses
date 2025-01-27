# Given a string, create a dictionary where keys are characters, and values are
# their ASCII values.

def string_to_ascii_dict(word):
    ascii_dict = {char: ord(char) for char in word}
    return ascii_dict

word = "Python"
result = string_to_ascii_dict(word)
print(f"ASCII dictionary is: {result}")
