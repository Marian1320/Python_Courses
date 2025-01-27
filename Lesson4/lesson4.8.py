# Input three integers. Output the word “Sorted” if the numbers are listed in
# a non-increasing or non-decreasing order and “Unsorted” otherwise.
a=int(input())
b=int(input())
c=int(input())

if a>=b>=c:
    print("Sorted")
elif a<=b<=c:
    print("Sorted")
else:
    print("Unsorted")