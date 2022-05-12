# Write a program that finds out whether a given name is present in a list or not.

l = [34 , 45 , 67 , 98 , 1 , 50]

a = int(input("Enter The Number : "))
if(l.count(a) > 0):
    print(a,"is present in the list")
else :
    print(a,"is not present in the list")