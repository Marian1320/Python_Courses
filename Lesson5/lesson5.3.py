# Write a Python program to get the smallest number from a list.

x=[1,2,3,4]
y=x[0]

for num in x:
    if num < y:
        y=num
print(y)

x=[5,7,3,9,11]
y=x[0]

for num in x:
    if num < y:
        y=num
print(y)

x=[25,1,1,3]
y=x[0]

for num in x:
    if num < y:
        y=num
print(y)

x=[1,2,1,1]
y=x[0]
for num in x:
    if num < y:
        y=num
print(y)
