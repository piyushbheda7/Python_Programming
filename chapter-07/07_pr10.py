 # Write a program to print the multiplication table of n using for loop in reversed order.

n = int(input("Enter a Number : "))

i = 10 
while i > 0 :
    print(f"{n} * {i} = {n*i}")
    i -= 1
