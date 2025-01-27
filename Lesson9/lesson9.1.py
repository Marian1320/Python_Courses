# Print the even numbers from 0 to 20 using a for loop and the range function

even_num=[]
for x in range(20):
    if x%2==0:
        even_num.append(x)
print(even_num)