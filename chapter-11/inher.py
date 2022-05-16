class Employee:
    a = 34

class Programmer(Employee):
    b = 32

pr = Programmer()
print(pr.a)
print(pr.b)

em = Employee()
print(em.a)
# print(em.b)  -> this will give an error because employee class doesn't contain b