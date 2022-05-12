# Write a program to calculate the grade of a student from his marks from the following scheme:

# 90-100	Ex
# 80-90	A
# 70-80	B
# 60-70	C
# 50-60	D
# <50	F

per = float(input("Enter Your Percentage : "))

if(per > 90 and per < 100) :
    print("You got Ex grade......")
elif(per > 80 and per < 90) :
    print("You got A grade......")
elif(per > 70 and per < 80) :
    print("You got B grade......")
elif(per > 60 and per < 70) :
    print("You got C grade......")
elif(per > 50 and per < 60) :
    print("You got D grade......")
else :
    print("You got F grade......")