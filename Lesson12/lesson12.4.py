# Write a function that finds the index of a given element in a list. If the element is not
# present, return -1.

def get_index(seq,element):
    for i in range(len(seq)):
        if seq[i]==element:
            return i
    return -1
print(get_index([1,2,3,4,5],3))