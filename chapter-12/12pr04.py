# Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ZeroDivisionError.

try:
    a = int(input("Enter a Number : "))
    b = int(input("Enter another Number : "))
    c = a/b
    print(f"{a}/{b} = {a/b}")
except ZeroDivisionError:
    print(f"{a}/0 = infinite")