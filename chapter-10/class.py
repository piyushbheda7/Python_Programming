class Employee : # name should be pascal case mean first letter is capital
    name = "Piyush "
    marks = 34
    center = "Baroda"

# -> this is the blank application give example in video it is like a form without written into it
# -> like blueprint of an object

MyApp = Employee() 
# it is an object initialization of class Employee
# Memory is allocated only after object instantiation
print(MyApp.marks)
print(MyApp.name)