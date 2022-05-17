# filter : filter creates a list or items for which the function reutrn true

from logging import Filterer


greater = lambda x : x>4
l = [1, 2, 3, 4, 8, 54, 67, 81, 89]
d = filter(greater , l)
print(list(d))