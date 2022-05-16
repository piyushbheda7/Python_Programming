from re import A


class Employee:
    def __init__(self , a , name ) :
        self.a = a
        self.name = name 

    def __truediv__(self , obj):
        return self.a * obj.a


    def __str__(self) -> str:
        return self.name

    def __len__(self):
        return len(self.name)

a = Employee(45 , 'Piyush')
b = Employee(40 , 'Rohan')

print(a / b)
print(a , b )
print(len(a))
print(len(b))