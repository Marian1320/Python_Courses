# Write a function that prints all prime numbers up to a given limit.

def is_prime(nums):
    if nums <= 1:
        return False
    i = 2
    while i*i <= nums:
        if nums % i == 0:
            return False
        i+=1
    return True

def prime_numbers_upto(n):
    for i in range(2, n + 1):
        if is_prime(i):
            print(i)


prime_numbers_upto(10)
