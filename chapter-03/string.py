b = "piyush's" # use this if you have single quotes in your strings

c = '''piyush"s and 
piyush's'''

print(b)
print(type(b))
print(c)

greeting = "Good Morning,"
name = "piyush"
c =greeting + name 
print(c[0])

# c[4] = 'd' --> does not work

print(c[0:3]) # here 0 is included but 3 is not

# print(c[1:4])

# print(c[-5:-1]) # same as c[:]
print("\n",c)
print(c[0::3])
print(c[0::4])