# We are going to write a program that generates a random number and asks the user to guess it.

# If the player’s guess is higher than the actual number, the program displays “Lower number please”. Similarly, if the user’s guess is too low, the program prints “higher number please”.

# When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.

# Hint: Use the random module 

import random


ran = random.randint(0,100)

# print(ran)

l = set()

user = int(input("Guess the Number : "))

while user != ran :
    if user > ran :
        # print()
        l.add(user)
        user = int(input("Lower Number Please....."))
        continue
    elif user < ran :
        l.add(user)
        user = int(input("Higher Number Please...."))
        continue

print("\nThe Number is : ", ran)
print("\nThe Number Which are Guesses By The Player is : ",l)