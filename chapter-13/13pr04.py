# Write a program to filter a list of numbers that are divisible by 5.

div = lambda x: x%5 == 0
l = [ 3 , 5, 22 , 60 , 75 , 2 , 54, 89, 55]
a = filter(div,l)
print(list(a))