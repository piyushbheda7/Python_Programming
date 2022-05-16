# Create a class C-2d vector and use it to create another class representing a 3-d vector.

from re import I
from traceback import print_tb


class C_2d:
    # a = 34
    # b = 96
    def __init__(self , i , j ) -> None:
        self.i = i
        self.j = j 
        # print("This is C_2d constructor")

    def printObj2d(self):
        print("This is C_2d Class") 

class C_3d(C_2d):
    c = 45
    def __init__(self , i , j , k) -> None:
        self.k = k
        super().__init__(i , j)
        # print("This is C_3d Constructor")

    def printObj3d(self):
        print("This is C_3d Class")

pqr = C_3d(10 , 20 , 30)
print(pqr.i)
print(pqr.j)
print(pqr.k)
pqr.printObj3d()
pqr.printObj2d()