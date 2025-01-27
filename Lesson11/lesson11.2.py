# Write a Python function to calculate count of each letter in string


def count_letters(input_str):
    letters={}
    for i in input_str:
        if i.isalpha():
            if i in letters:
                letters[i]+=1
            else:
                letters[i]=1
    return letters
print(count_letters('abrakadabra'))