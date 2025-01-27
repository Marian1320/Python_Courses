# You are given four real numbers- a1, b1, a2, b2 - The endpoints of two
# line segments on a line. Find the length of their intersection. Note that the
# order of the endpoints of a segment is irrelevant, i.e. the segments [1;2]
# and [2;1] are considered the same.

a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())

start1 = min(a1, b1)
end1 = max(a1, b1)
start2 = min(a2, b2)
end2 = max(a2, b2)

i_start = max(start1, start2)
i_end = min(end1, end2)

if i_start < i_end:
    length = i_end - i_start
else:
    length = 0

print(length)
