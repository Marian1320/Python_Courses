# Write a Python program that calculates the Fibonacci sequence up to a
# given number n using a while loop. The Fibonacci sequence is a series of numbers
# where each number is the sum of the two preceding ones.


x = int(input())

i, j = 0, 1

fibonacci = []

while i <= x:
    fibonacci.append(i)
    i, j = j, i + j

print(fibonacci)
