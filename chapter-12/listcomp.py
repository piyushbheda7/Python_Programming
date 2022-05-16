# list comprehensions : list comprehensions is an elegant way to create lists based on existing lists

l = [ 1 , 2,  3 , 4 , 5 , 6]
l2 = []

for item in l:
    l2.append(item*item)

print(l2)

l3 = [ i for i in l if i > 3]
print(l3)