# map : map applies a function to all the items in an input list

square = lambda x: x*x
l = [1, 2, 3, 4, 5]
c = map(square , l)
print(list(c))
