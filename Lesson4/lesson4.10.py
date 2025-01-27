# Given the salaries of three employees working at a department, find the
# amount of money by which the salary of the highest-paid employee differs
# from the salary of the lowest-paid employee. The input consists of three
# positive integers - the salaries of the employees. Output a single number,
# the difference between the top and the bottom salaries

a=int(input())
b=int(input())
c=int(input())

if a>b>c:
    print(a-c)
elif a>c>b:
    print(a-b)
elif b>a>c:
    print(b-c)
elif b>c>a:
    print(b-a)
elif c>a>b:
    print(c-b)
else:
    print(c-a)