# Write a function that removes an element at a specified index from a list. Handle the
# IndexError by raising a custom exception if the index is out of range.
from logging import exception
def remove_element_at_index(my_list, index):
    try:
        removed_element = my_list.pop(index)
        print(f"Removed element: {removed_element}")
    except IndexError:
        raise IndexError(f"Error: Index {index} is out of range.")

my_list = [10, 20, 30, 40, 50]

remove_element_at_index(my_list, 2)
print(my_list)



