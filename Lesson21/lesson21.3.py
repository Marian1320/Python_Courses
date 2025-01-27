# Given a list of numbers, write a function to nd the sum of all numbers in the list that
# can be divided by 7.

def sum_divisible_by_7(numbers):
    return sum(number
               for number in numbers
               if number % 7 == 0)


numbers = [14, 3, 21]
result = sum_divisible_by_7(numbers)
print(f"Sum of numbers divisible by 7: {result}")
