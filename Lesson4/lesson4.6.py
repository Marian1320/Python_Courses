# Input two positive integers, and
# output a line describing their relation. Follow the sample format.

a = int(input())
b = int(input())

if a > b:
    print(str(a) + ">" + str(b))
elif a < b:
    print(str(a) + "<" + str(b))
else:
    print(str(a) + "==" + str(b))

