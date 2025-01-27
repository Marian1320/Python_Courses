# Write a Python program to find the second smallest number in a list.

x = [1, 9, 3, 4]
smallest = float('inf')
second_smallest = float('inf')

for num in x:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif smallest < num < second_smallest:
        second_smallest = num

if second_smallest == float('inf'):
    print("No second smallest exists.")
else:
    print( second_smallest)
