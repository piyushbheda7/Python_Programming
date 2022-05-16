# The method name with @property decorator is called getter method

# we can define a function as @name.setter decorator for setter method

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

    @length.setter
    def length(self, value):
        self.a = value
        
emp = employee()
emp.setAttr(1 , 2 , 3)
print(emp.length) # -> the function can call without the paranthese of property method
emp.length = 78 # cannot make any sense without @length.setter method
print(emp.length) # the method can use like using the attributes 
print(emp.a)