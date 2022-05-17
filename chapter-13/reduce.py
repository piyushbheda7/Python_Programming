# reduce : reduce applies a rolling computation to sequential pair of elements

from functools import reduce

sum = lambda x, y : x + y
a = [1, 2, 3, 4, 5]
d = reduce(sum , a)
print(d)