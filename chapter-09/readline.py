f = open('sample.txt' , 'r')

# read first line
# data = f.readline()
# print(data)

# read second line
# data1 = f.readline()
# print(data1)


datalist = f.readlines()

print(datalist)

f.close()