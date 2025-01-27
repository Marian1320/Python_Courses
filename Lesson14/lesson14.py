# Write a function in python to read the content from a text file "example.txt" line by
# line and display the same on screen.

with open("text.txt", "r") as file:
    line = file.readline()
    while line:
        print(line)
        line = file.readline()
