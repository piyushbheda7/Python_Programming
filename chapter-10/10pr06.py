# Can you change the self parameter inside a class to something else (say ‘harry’)? Try changing self to ‘slf’ or ‘harry’ and see the effects.

# Create a class programmer for storing information of a few programmers working at Microsoft.

from multiprocessing import Manager


class MicroSoftEmployee:
    def __init__(slf , name , id , salary , Role):
        slf.name = name 
        slf.id = id 
        slf.salary = salary
        slf.Role = Role
    
    def printInfo(slf):
        print(f"{slf.name}'s\nid : {slf.id} \nsalary : {slf.salary} \nRole :  {slf.Role}\n")
    
Rohan = MicroSoftEmployee('Rohan',3205,50000,'developer')
Milan = MicroSoftEmployee('Milan',3505,45000,'Q&A')
Nitin = MicroSoftEmployee('Nitin' , 52010 , 80000 , 'Manager')

Rohan.printInfo()
Milan.printInfo()
Nitin.printInfo()

# -> yes we can change the self to slf or anything else