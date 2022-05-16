# Write a list comprehension to print a list that contains the multiplication table of a user-entered number

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = int(input("Enter a number :"))

l1 = [ a*i for i in l]

print(l1)