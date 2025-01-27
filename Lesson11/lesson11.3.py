# Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.

def factorial(arg):
    result=1
    for i in range(1, arg+1):
        result*=i
    return result
print(factorial(5))