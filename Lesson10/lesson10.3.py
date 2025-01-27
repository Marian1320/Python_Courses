# Write a Python program that calculates
# the sum of all even numbers between 1 and 100 using a while loop.

i=1
s=0

while i<=100:
    if i%2==0:
        s+=i
    i+=1
print(s)

