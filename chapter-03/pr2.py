# Write a program to fill in a letter template given below with name and date.

letter = '''Dear <|Name|>,
You are Selected!

Date: <|Date|>'''

name = input("Enter Your Name :")
date = input("Enter the Date :")

letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)

# letter = '''Dear''' + name +''',
# You are selected!

# Date: '''+date
print(letter)