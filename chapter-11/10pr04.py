# Write a class complex to represent complex numbers, along with overloaded operators + and * which adds and multiplies them.

import imghdr
from operator import concat


class Complex:
    def __init__(self , a , b) -> None:
        self.a = a
        self.b = b

    # def __str__(self):
    #     return concat(self.real,'i','+',self.img,'j')

    def __add__(self , obj):
        return Complex(self.a + obj.a , self.b + obj.b)

c1 = complex(20 , 30)
c2 = complex(11 , 3)

c = c1 + c2 
print(c)