# Write a function that calculates the square root of a number using the math module.

import math
def square_root(num):
    if num < 0:
        return None
    else:
        return math.sqrt(num)

print(square_root(4))