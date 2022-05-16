class employee:
    a = 1
    b = 4
    c = 6
    @classmethod # it is used to changes in the class attributes
    def setAttr(cls , a , b , c):
        cls.a = a
        cls.b = b 
        cls.c = c

emp = employee()
print(employee.a)
print(employee.b)
print(employee.c)
emp.setAttr(1 , 2 , 3)
print(employee.a)
print(employee.b)
print(employee.c)

xyz = employee()
print(xyz.a)
print(xyz.b)
print(xyz.c)