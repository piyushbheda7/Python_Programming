# Write a class calculator capable of finding square, cube, and the square root of a number

from cmath import sqrt


class Calculator:
    def square(self , number):
        return number * number 
    
    def cube(self , number):
        return number * number * number 
    
    def square_root(self , number):
        return sqrt(number).real

num = int(input("Enter the Number : "))

MyCalculator = Calculator()

print(f"The Square of {num} is {MyCalculator.square(num)}")
print(f"The cube of {num} is {MyCalculator.cube(num)}")
print(f"The Square-root of {num} is {MyCalculator.square_root(num)}")