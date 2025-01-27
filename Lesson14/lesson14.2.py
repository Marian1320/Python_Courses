# Implement a Python program that reads a text file (input.txt),
# prompts the user for a word to find, and another word to replace it with.
# Replace all occurrences of the first word with the second word and
# save the modified text to a new file (output.txt).

with open("text.txt", "r") as file:
    content = file.read()


word_to_find = input("enter current word:")
word_to_replace = input("enter new word:")

modified_content = content.replace(word_to_find, word_to_replace)

with open("output.txt", "w") as file:
    file.write(modified_content)

print("output.txt")
