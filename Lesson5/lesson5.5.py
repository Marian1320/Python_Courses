# Write a Python program to remove duplicates from a list.
x=[1,2,3,1]
u=[]

for num in x:
    if num not in u:
        u.append(num)
print(u)

x=[5,7,3,9,11]
u=[]

for num in x:
    if num not in u:
        u.append(num)
print(u)

x=[25,1,1,13]
u=[]

for num in x:
    if num not in u:
        u.append(num)
print(u)