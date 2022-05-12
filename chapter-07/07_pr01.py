# Write a program to print the multiplication table of a given number using for loop.

a = int(input("Enter the Number : "))

for i in range (1,11) :
    # print(a,"*",i,"=",(a*i))
    print(str(a) + " X " + str(i) + " = " + str(a*i))
    print(f"{a}X{i}={a*i}")