# Write a program to input name, marks and phone number of a student and format it using the format function like below:
# “The name of the student is Harry, his marks are 72 and the phone number is 99999888”

name = input("Enter Your name : ")
marks = input("Enter Your Marks : ")
PhoneNo = input("Enter Your Phone Number : ")

str = '\nThe name of the studet is {}, \nhis marks are {} and \nthe phone number is {}'.format(name , marks , PhoneNo)

print(str)