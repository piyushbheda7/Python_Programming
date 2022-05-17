# A list contains the multiplication table of 7. Write a program to convert it to a vertical string of the same numbers (7,14,….)

l = [ 7 , 14 , 21 , 28 , 35 , 42 , 49 , 56 , 63 , 70]

st = ''
for item in l:
    st += str(item) +'\n'

print(st)