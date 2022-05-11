# Replace the double spaces from problem 3 with single spaces.

story = "this is the story about a lion who live in a jungle with the many animals like elephant , rat , rabbits , fox and many  more ........."

print(len(story))

story = story.replace("  "," ")

print(len(story))
print(story)