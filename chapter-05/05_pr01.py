# Write a program to create a dictionary of Hindi words with values as their English translation. Provide the user with an option to look it up!

HindiDict = {
    "tum" : "you" ,
    "mein" : "i" ,
    "kya" : "what" ,
    "kab" : "when" ,
    "pankha" : "fan" ,
    "dabba" : "box" ,
    "vastu" : "thing"
}

print("options are : ",list(HindiDict.keys()))

a = input("Enter the Hindi dictionary word : ")

print("the English translation word of ",a,"is ",HindiDict[a])

print("the English translation word of ",a,"is ",HindiDict.get(a))