myDict = {
    "fast" : "In a quick manner" ,
    "Harry" : "A Coder" ,
    "harry" : "This is also Coder" ,
    "Marks" : [1 , 2 , 3 ] ,
    "marks" : (1 , 2 , 3) ,
    "anotherdict" : {"harry" : "player"} ,
     1 : 2
}

print(myDict.items()) # type of dictionary items is dict_items 
# prints the key , value of the dictionary in form of tuples
print("\n")
print(myDict.keys())
print("\n")
print(type(myDict.keys())) # type of dictionary keys is dict_keys
print(list(myDict.keys())) # can change the dict_keys to list
print(myDict.values())

updateDict = {
    "Lovish" : "friend",
    "mark" : 99
}

myDict.update(updateDict)
print(myDict)

print(myDict.get("harry"))
print(myDict['harry']) # both will give same result

print(myDict.get('harry2')) # this will not generets error -> it returns none if ont present in dictionary
print(myDict['harry2']) # this will generates error