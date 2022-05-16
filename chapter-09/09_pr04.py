# A file contains the word “Donkey” multiple times. You need to write a program which replaces this word with ###### by updating the same file.

with open('pr04.txt','r') as f:
    data = f.read()
    with open('pr04.txt' , 'w') as w:
        w.write(data.replace('donkey','######'))