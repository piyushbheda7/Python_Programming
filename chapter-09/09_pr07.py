# Write a program to find out the line number where python is present from question 6.

with open('pr06.txt','r') as f:
    l = f.readline()
    if 'python' in l:
        print('Python is in 1st line.')
    l = f.readline()
    if 'python' in l:
        print('Python is in 2nd line.')
    l = f.readline()
    if 'python' in l:
        print('Python is in 3rd line.')
    l = f.readline()
    if 'python' in l:
        print('Python is in 4th line.')
    l = f.readline()
    if 'python' in l:
        print('Python is in 5th line.')
    l = f.readline()
    if 'python' in l:
        print('Python is in 6th line.')