# use open function to read the content of a file!
# f = open('sample.txt' , 'r')

f = open('sample.txt' )  # vy default the mode is r

# data = f.read()
data1 = f.read(5) # it will read first 5 characters

# print(data)
print(data1)

f.close()