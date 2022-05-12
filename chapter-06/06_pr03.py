# A spam comment is defined as a text containing the following keywords:
# “make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

text = input("Enter the text : ")

if(text == 'click this'):
    print("This Text is a Spam Text......")
elif(text == 'make a lot of money'):
    print("This Text is a Spam Text......")
elif(text == 'buy now'):
    print("This Text is a Spam Text......")
elif(text == 'subscribe this'):
    print("This Text is a Spam Text......")
else :
    print(text,"......")