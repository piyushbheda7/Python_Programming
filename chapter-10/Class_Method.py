class Employee : 
    name = "Piyush "
    marks = 34
    center = "Baroda"

    def printObj(self):
        print(f"The Name is {self.name}")

    @staticmethod
    def greet():
        print("Good Day")

Employee.greet() #-> static method doesn't require object to execute
MyApp = Employee()
print(MyApp.marks)
print(MyApp.name)
MyApp.printObj()