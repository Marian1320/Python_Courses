# Write a Python program to square and cube every number in a given list of
# integers using Lambda.

square = lambda x: x**2
cube = lambda x: x**3
nums = [1, 2, 3, 4, 5]
result_square = list(map(square, nums))
result_cube = list(map(cube, nums))
print((result_square, result_cube))
