# Write a function that swaps the values of two tuples.

tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
def swap_tuples(tuple1, tuple2):
    return tuple2, tuple1

swapped_tuple1, swapped_tuple2 = swap_tuples(tuple1, tuple2)

print(f"Swapped Tuple 1: {swapped_tuple1}")
print(f"Swapped Tuple 2: {swapped_tuple2}")

