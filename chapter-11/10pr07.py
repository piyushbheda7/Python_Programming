# Override the __len__() method on vector of problem 5 to display the dimension of the vector.

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

    def __len__(self):
        return len(self.data)

v1 = vector([10 , 20 , 30])
v2 = vector([20 , 30 , 40])

v = v1 * v2
print("Length of new vector is ",len(v))
print(v.dim)
