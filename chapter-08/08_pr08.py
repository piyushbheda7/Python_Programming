# Write a python function to print the multiplication table of a given number.

def MultiplicationTable(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

n = int(input("Enter a Number : "))

MultiplicationTable(n)