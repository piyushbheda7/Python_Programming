# Write a program to calculate the factorial of a given number using for loop.

from re import I


n = int(input("Enter a Number : "))

fact = 1
for i in range(1,n+1):
    fact *= i

print(f"factorial of {n} is {fact}")