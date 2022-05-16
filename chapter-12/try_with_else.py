
from ast import Try

try:
    print("Hello User .......")
    a = int(input("Enter a NUmber : "))
    b = int(input("Enter another Number : "))
    c = a / b
    print("the Division is ",c)

except ValueError as ve:
    print(ve)
except ZeroDivisionError as zde:
    print(zde)
except Exception as e :
    print(e)
else:
    print("Try was Successful....")

print("...............< End of Code >..............")