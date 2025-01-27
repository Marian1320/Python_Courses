# Print the multiplication table of 5 using a for loop and f”strings”.
# The table should be printed up to 10.

table=""
for x in range(1,11,1):
    table=x*5
    print(f"{x} * 5 =",table)