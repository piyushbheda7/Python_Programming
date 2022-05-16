# Write a program to find out whether a file is identical and matches the content of another file.

with open('pr091.txt','r') as f:
    data1 = f.read()

with open('pr092.txt','r') as f1:
    data2 = f1.read()

if data1 == data2:
    print("the content of both files are same")
else:
    print("The Content of both files are not same")