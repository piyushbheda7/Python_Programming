# write a program to print the following star pattern:

# * * *
# *   *             #For n=3
# * * * 

from django.urls import clear_script_prefix


n = int(input("Enter a Number : "))

for i in range(n) :
    # for j in range(n) :
    if(i == 0) :
        print("*" * n,end="")
    elif(i == (n-1)) :
        print("*" * n,end="")
    else :
        print("*",end="")
        print(" " * (n-2),end="")
        print("*",end="")
    print()