# Write a program to read the text from a given file, “poems.txt” and find out whether it contains the word ‘twinkle’.

with open('poems.txt' , 'r') as f:
    data = f.read()

if data.find('twinkle') > -1 : 
    print("Yes , file contains the word 'twinkle'")
else:
    print("N0 , File doesn't contains the word 'twinkle'")