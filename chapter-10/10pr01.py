# Create a class programmer for storing information of a few programmers working at Microsoft.

from multiprocessing import Manager


class MicroSoftEmployee:
    def __init__(self , name , id , salary , Role):
        self.name = name 
        self.id = id 
        self.salary = salary
        self.Role = Role
    
    def printInfo(self):
        print(f"{self.name}'s\nid : {self.id} \nsalary : {self.salary} \nRole :  {self.Role}\n")
    
Rohan = MicroSoftEmployee('Rohan',3205,50000,'developer')
Milan = MicroSoftEmployee('Milan',3505,45000,'Q&A')
Nitin = MicroSoftEmployee('Nitin' , 52010 , 80000 , 'Manager')

Rohan.printInfo()
Milan.printInfo()
Nitin.printInfo()