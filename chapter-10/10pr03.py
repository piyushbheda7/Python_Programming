# Create a class with a class attribute a; create an object from it and set a directly using object.a=0 Does this change the class attribute?

class change:
    a = 625

xyz = change()
print(xyz.a)
xyz.a = 610 
print(xyz.a)

pqr = change()
print(pqr.a)

# it does not change the class attribute