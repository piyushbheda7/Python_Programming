# Write a program to print the following star pattern.
#     *
#   ***  
# ***** for n=3

n = int(input("Enter a Number : "))

for i in range(0,n) :
    # for j in range(0,(n-i-1)) :
    print(" " * (n-i-1), end="")
    # for j1 in range(0,((2*i)+1)):
    print("*" * (2*i+1), end ="")
    print(" " * (n-i-1))
    