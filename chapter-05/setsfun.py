s = set()

s.add(23)
s.add(50)
s.add((1 , 2 , 3 , 4 , 5)) 
s.add('harry')
print(s)

# return the length of set
print(len(s))

# remove the element which value is 'harry'
s.remove('harry')
print(s)

# removes an arbitrary element from the set and returns the element removed 
print(s.pop())

# returns a new set with all items from both sets
print(s.union({8 , 50}))

# returns a set which contains only items in both sets
print(s.intersection({8 , 23}))

# clear
s.clear()
print(s)