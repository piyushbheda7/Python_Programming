# Write a program to input eight numbers from the user and display all the unique numbers (once).

s = set()

s.add(int(input("Enter the 1st Number : ")))
s.add(int(input("Enter the 2nd Number : ")))
s.add(int(input("Enter the 3rd Number : ")))
s.add(int(input("Enter the 4th Number : ")))
s.add(int(input("Enter the 5th Number : ")))
s.add(int(input("Enter the 6th Number : ")))
s.add(int(input("Enter the 7th Number : ")))
s.add(int(input("Enter the 8th Number : ")))

print("The Unique Numbers are :",list(s))