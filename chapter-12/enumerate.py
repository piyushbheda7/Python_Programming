a = [1  , 4 , 6 , 'apple']
i = 0 
for item in a:
    i = i + 1
    print(f"Item umber {i} is {item}")

for i , item in enumerate(a):
    print(f"Item umber {i+1} is {item}")