# Write a python function to print the first n lines of the following pattern.
# ***
# **       #For n = 3
# *

def pattern(n):
    for i in range(n):
            print("*" * (n-i))

a = int(input("Enter a Number : "))

pattern(a)