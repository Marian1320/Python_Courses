# Append new string in the middle of a given (even number of characters) string

x='python'
y=x[:len(x)//2]+'new'+x[len(x)//2:]
print(y)