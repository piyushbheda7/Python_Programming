# Write a program to find the greatest of four numbers entered by the user.

a = int(input("Enter Number 1:"))
b = int(input("Enter Number 2:"))
c = int(input("Enter Number 3:"))
d = int(input("Enter Number 4:"))

if(a > b and a > c and a > d) :
    print(a,"is greatest Number ")
elif(b > a and b > c and b > d) :
    print(b,"is greatest Number ")
elif(c > a and c > b and c > d) :
    print(c,"is greatest Number ")
else :
    print(d,"is greatest Number ")