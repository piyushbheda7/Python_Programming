class parent:
    a = 4 
    def __init__(self):
        print("parent")
class child1(parent):
    b = 2
    def __init__(self):
        super().__init__()
        print("child1")
class child2(child1):
    c = 9  
    def __init__(self):
        super().__init__()
        print("child2")

ch = child2()
print(ch.a)
print(ch.b)
print(ch.c)