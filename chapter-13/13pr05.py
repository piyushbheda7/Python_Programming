# Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce
import math


maxi = lambda x , y :  max(x , y)
l = [1 , 7, 55 , 19 , 39  , 54 , 89]
a = reduce(maxi,l)
print(a)