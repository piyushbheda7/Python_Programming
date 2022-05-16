# Write a program to print the third, fifth, and seventh elements from a list using the enumerate function

l = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i, item in enumerate(l):
    if i+1 == 3 or i+1 == 5 or i+1 == 7:
        print(f"{i+1} : {item}")