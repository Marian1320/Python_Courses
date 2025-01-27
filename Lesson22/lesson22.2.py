# Given a string, create a dictionary where keys are characters and values are their
# frequencies in the string.

def char_frequencies(input_string):
    freq_dict = {char: input_string.count(char) for char in set(input_string)}
    return freq_dict

input_string = "Mariana"
result = char_frequencies(input_string)
print(f"Character frequencies for '{input_string}': {result}")

