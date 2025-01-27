# Write a function that returns the nth largest element from a list.

def nth_largest(numbers, n):
    if n < 1 or n > len(numbers):
        raise ValueError("n must be between 1 and the len")

    sorted_numbers = sorted(numbers, reverse=True)

    return sorted_numbers[n - 1]


nums = [4, 2, 9, 7, 5, 8, 1]

print(nth_largest(nums, 2))