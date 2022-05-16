class Employee : 
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks 
        

    def printObj(self):
        print(f"The Name is {self.name}")
        print(f"The marks is {self.marks}")

MyApp = Employee('piyush' , 60)
rohan = Employee('rohan' , 50)
MyApp.printObj()
rohan.printObj()