class parent:
    a = 4

class child1(parent):
    b = 2

class child2(child1):
    c = 9

ch = child2()
print(ch.a)
print(ch.b)
print(ch.c)