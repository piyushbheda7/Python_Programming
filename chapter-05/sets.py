
# below will creates empty dictionary
b = {}
print(type(b))

# below will creates empty set
c = set()
print(type(c))

s = set()

# adding values to an empty set
s.add(23)
s.add(50)
# s.add([1 , 2 , 3 , 4 ]) -> we can't add list or dictionary into set
s.add((1 , 2 , 3 , 4 , 5)) # we can add tuples into set
print(s)