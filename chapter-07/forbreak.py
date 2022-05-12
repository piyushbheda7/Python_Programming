l = [ 1 , 6 , 23 , 56]

# this is for break keyword used in for loop
for i in l :
    print(i)
    if(i == 23):
        break

# this is for continue keyword used in for loop
for j in l :
    if(j == 23) :
        continue
    print(j)

# this is for pass keyword used in for loop
for item in l :
    pass
print(item)