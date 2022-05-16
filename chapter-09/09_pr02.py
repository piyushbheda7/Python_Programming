# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file “Hiscore.txt” which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever game() breaks the Hi-Score.

import random

def game() :
    return random.randint(0,999)

score = game()

with open('score.txt','r') as f:
    hiscore = f.read()

new = game()

if hiscore =='':
    with open('score.txt' , 'w') as wr:
        wr.write(str(new))
elif(new > int(hiscore) or hiscore == ""):
    with open('score.txt' , 'w') as wr:
        wr.write(str(new))
        





