# Write a Python script that takes multiple text files as input and concatenates their
# contents into a single text file.
# List of input files
files = ["text1.txt", "text2.txt"]
merged_file = "merged.txt"
with open(merged_file, "w") as outfile:
    for file_name in files:
        with open(file_name, "r") as infile:
            outfile.write(infile.read() + "\n")

print("merged_file")

