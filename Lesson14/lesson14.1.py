# Write a Python script that reads a text file (input.txt) and
# counts the occurrences of each character (including spaces and punctuation).
# Output the character frequency to another text file (output.txt).

with open('text.txt', "r") as file:
    symbols = list(file.read())
    each_symbol = {}
    for char in symbols:
        if char in each_symbol:
            each_symbol[char] += 1
        else:
            each_symbol[char] = 1

with open('output.txt', 'w') as output_file:
    for char, count in each_symbol.items():
        output_file.write(f"'{char}': {count}\n")
print("output.txt")



