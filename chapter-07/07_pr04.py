# Write a program to find whether a given number is prime or not.

n = int(input("Enter a Number : "))

flag = 0 
for i in range(2,n) :
    if(n%i == 0) :
        flag = 1
        print(n,"is not a prime Number")
        break

if(flag == 0) :
    print(n,"is prime Number")