# Write a Python program to add two given lists using map and
# lambda

sum_of_lists=lambda a, b: a+b
a=[1,2,3]
b=[4,5,6]
result=list(map(sum_of_lists,a,b))
print(result)