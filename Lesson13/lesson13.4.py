# Write a Python program to find intersection of two given arrays using
# Lambda.

intersection_of_arrays=lambda a, b: a&b
a={1,2,3,5,7,8,9,10}
b={1,2,4,8,9}
print(list(intersection_of_arrays(a,b)))