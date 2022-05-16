class parent1:
    a = 4

class parent2:
    b = 2

class child(parent1 , parent2):
    c = 9

ch = child()
print(ch.a)
print(ch.b)
print(ch.c)