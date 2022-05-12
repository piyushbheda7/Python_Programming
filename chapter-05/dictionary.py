myDict = {
    "fast" : "In a quick manner" ,
    "Harry" : "A Coder" ,
    "harry" : "This is also Coder" ,
    "Marks" : [1 , 2 , 3 ] ,
    "marks" : (1 , 2 , 3) ,
    "anotherdict" : {"harry" : "player"}
}

# Access the elements of Dictionary 
print(myDict)
print(myDict['fast'])
print(myDict['Harry'])
print(myDict['harry'])
print(myDict['anotherdict'])

# Change in the elements of Dictionary
myDict['harry'] = 'piyush'
print(myDict['harry'])