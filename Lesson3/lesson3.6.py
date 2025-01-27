#6. Write a Python function to get a string made of its first three characters of a specified string.
# If the length of the string is less than 3 then return the original string.

x='python'
if len(x)<=3: x=x
else: x=x[:3]
print(x)