#2.	Write a Python program to add 'ing' at the end of a given string (length should be
# at least 3). If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.

x='abc'
if len(x)>=3: x=x + 'ing'
print(x)

x='string'
if x[-3:]=='ing': x=x + 'ly'
print(x)