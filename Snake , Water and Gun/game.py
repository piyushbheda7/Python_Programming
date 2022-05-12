# Snake vs  Water : snake wins
# Water Vs Gun : Water wins
# Snake vs Gun : Gun wins


from inspect import walktree
from logging.handlers import WatchedFileHandler


# 1 - Snake
# 2 - Water
# 3 - Gun

import random

print("\nSnake(1) - Water(2) - Gun(3)")

l = [ 1 , 2 , 3]

a = random.choice(l)

ch = int(input("\nEnter Your Choice From above Options in Number : "))

if ch == a :
    if ch == 1: 
        print("\ngame is Draw")
        print("\nYou both select Snake")
    elif ch == 2:
        print("\ngame is Draw")
        print("\nYou both select Water")
    else:
        print("\ngame is Draw")
        print("\nYou both select Gun")
elif ch == 1:
    if a == 2:
        print("\nYou Won!")
        print("\nYou Select - Snake & Machine Select - Water")
    else:
        print("\nYou Loose!")
        print("\nYou Select - Snake & Machine Select - Gun")
elif ch == 2:
    if a == 1:
        print("\nYou Loose!")
        print("\nYou Select - Water & Machine Select - Snake")
    else:
        print("\nYou Won!")
        print("\nYou Select - Water & Machine Select - Gun")
else:
    if a == 1:
        print("\nYou Won!")
        print("\nYou Select - Gun & Machine Select - Snake")
    else:
        print("\nYou Loose!")
        print("\nYou Select - Gun & Machine Select - Water")