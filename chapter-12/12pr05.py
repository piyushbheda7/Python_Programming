# Store the multiplication tables generated in problem 3 in a file named Tables.txt.

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# a = int(input("Enter a Number : "))

# with open('chapter-12/Tables.txt','w') as f:
#     for i in range(1 , 11):
#         f.write(f"{a} * {i} = {a*i}\n")

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = int(input("Enter a number :"))

l1 = [ a*i for i in l]

with open('chapter-12/Tables.txt','w') as f:
    f.write(str(l1))
