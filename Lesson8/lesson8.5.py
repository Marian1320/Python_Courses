# You are given three lists, list1, list2, and list3. Your task is to implement a
# program that takes these lists and prints the following:
# The set of elements that are common to all three lists.
# The set of elements that are present in at least two of the three lists, but not in all
# three.
# The set of elements that are unique to each list (present in only one list).

a={1,2,3,4,5,6}
b={4,5,6,7,8,9}
c={3,4,5,10}
d=a | b
print(f'common to all three lists: {d|c}')

e=a & b
f=a & c
g=b & c
h=e|f
print(f'present in at least two of the three lists {h|g}')

i=d|c
j=h|g
print(f'unique to each list {i-j}')