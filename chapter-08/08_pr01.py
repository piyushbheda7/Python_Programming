# Write a program using the function to find the greatest of three numbers.

def greatest(num1,num2,num3):
    if(num1 > num2 and num1 > num3):
        return num1
    elif(num2 > num1 and num2 > num3):
        return num2
    else:
        return num3

a = int(input("Enter a number 1 : "))
b = int(input("Enter a number 2 : "))
c = int(input("Enter a number 3 : "))

print(f"The greatest Number is {greatest(a,b,c)}")