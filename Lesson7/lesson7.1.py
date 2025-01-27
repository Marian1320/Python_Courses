#Arrange string characters such that lowercase letters should come first
word="PyNaTive"

low_case = []
upper_case = []

for char in word:
    if char.islower():
        low_case.append(char)
    elif char.isupper():
        upper_case.append(char)

result = "".join(low_case + upper_case)

print(result)
