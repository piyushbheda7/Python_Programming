
from ast import Try

try:
    print("Hello User .......")
    a = int(input("Enter a NUmber : "))
    b = int(input("Enter another Number : "))
    c = a / b
    if b > a :
        raise Exception("The Divisor should not Be Less than Divider.........")
    print("the Division is ",c)

except ValueError as ve:
    print(ve)
except ZeroDivisionError as zde:
    print(zde)
except Exception as e :
    print(e)

print("...............< End of Code >..............")