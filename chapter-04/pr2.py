# Write a program to accept the marks of 6 students and display them in a sorted manner.

marks = []

marks.append(int(input("Enter The Marks Of 1st Student : ")))
marks.append(int(input("Enter The Marks Of 2nd Student : ")))
marks.append(int(input("Enter The Marks Of 3rd Student : ")))
marks.append(int(input("Enter The Marks Of 4th Student : ")))
marks.append(int(input("Enter The Marks Of 5th Student : ")))
marks.append(int(input("Enter The Marks Of 6th Student : ")))

marks.sort()
print(marks)