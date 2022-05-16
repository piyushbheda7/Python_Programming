class Employee : 
    name = "Piyush " # a class attribute
    marks = 34
    center = "Baroda"

    def printObj(self):
        print(f"The Name is {self.name}")

MyApp = Employee()
print(MyApp.marks)
print(MyApp.name)
MyApp.printObj() # -> this both are same because we using self as parameter in printobj functions
Employee.printObj(MyApp)

shyam = Employee()
shyam.name = 'shyam' # setting up a instance attribute
print(shyam.name)