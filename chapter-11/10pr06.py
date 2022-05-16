# Write __str__() method to print the vector as follows:
# 7i + 8j + 10k

from msvcrt import kbhit


class vector:
    def __init__(self , i , j , k) -> None:
        self.i = i 
        self.j = j 
        self.k = k

    def __str__(self ) -> str:
        return str(f"{self.i}i + {self.j}j + {self.k}k")

v = vector(10 , 20 , 30 )

print(v)