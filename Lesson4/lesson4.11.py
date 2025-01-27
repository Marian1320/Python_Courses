# Given a real number, round it to the nearest whole.

x=float(input())

n=int(x)
f=x-int(x)
if f>0.5:
    print(int(x)+1)
else:
    print(int(x))