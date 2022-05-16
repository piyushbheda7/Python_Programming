class employee:
    a = 1
    b = 4
    c = 6
    @classmethod # it is used to changes in the class attributes
    def setAttr(cls , a , b , c):
        cls.a = a
        cls.b = b 
        cls.c = c
    @property
    def length(self):
        return self.a

emp = employee()
emp.setAttr(1 , 2 , 3)
print(emp.length) # -> the function can call without the paranthese of property method