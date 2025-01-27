# Write a function that calculates the sum of squares of numbers from 1 to n.
def sum_of_square(number):
    sum_of_squares=0
    for i in range(1,number+1):
        sum_of_squares+=i*i
    return sum_of_squares
number=3
print(sum_of_square(number))
