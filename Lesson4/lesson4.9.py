# You are given four real numbers - the coordinates of two points on a
# plane. The first two numbers are the x and y coordinates of the first point,
# and the last two numbers are the x and y coordinates of the second point.
# Output the length of the line segment bounded by the two points.

a=int(input())
b=int(input())
c=int(input())
d=int(input())

x=(c-a)**2+(d-b)**2
print(x**0.5)
