# Write a class vector representing a vector of n dimension. Overload the + and * operator which calculates the sum and the dot product of them.

# This is for the two dimenstional vector

# class vector :
#     def __init__(self , i , j ) -> None:
#         self.i = i 
#         self.j = j 
#     def __add__(self , obj):
#         return vector(self.i + obj.i , self.j + obj.j)

#     def __mul__(self , obj):
#         return vector(self.i * obj.i , self.j * obj.j)

# v1 = vector(10 , 20)
# v2 = vector(20 , 30)

# v = v1 + v2
# print(v.i , v.j)

# v = v1 * v2
# print(v.i , v.j)

# This is for the N Dimenstionl vector

class vector:
    def __init__(self , l) -> None:
        self.dim = len(l)
        self.data = l

    def __add__(self , obj):
        myList = []
        for i in range(len(self.data)):
            myList.append(self.data[i] + obj.data[i])
        
        return vector(myList)
    
    def __mul__(self , obj):
        myList = []
        for i in range(len(self.data)):
            myList.append(self.data[i] * obj.data[i])
        
        return vector(myList)


v1 = vector([10 , 20 , 30])
v2 = vector([20 , 30 , 40])

v = v1 * v2
print(v.data)