# Write a function that takes two lists and returns a new list containing only the common
# elements. (without using set)

def common_elements(list1, list2):
    return [element for element in list1 if element in list2]

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = common_elements(list1, list2)
print(f"Common elements are: {result}")
