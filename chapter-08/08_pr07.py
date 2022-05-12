# Write a python function to remove a given word from a list and strip it at the same time.

def remove_and_split(string , word):
    newStr = string.replace(word , "")
    return newStr.strip()

this =  "          Piyush is a good programmer      "

print(remove_and_split(this , "Piyush"))
print(this)
print(this.strip())
