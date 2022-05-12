# Write a program to find the sum of first n natural numbers using a while loop.

n = int(input("Enter a Number : "))

sum = 0
i = 1
while i < n+1:
    sum = sum + i
    i += 1

print("The Sum Of first",n,"natural number is",sum)