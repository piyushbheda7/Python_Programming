# Write a program to find out whether a student is pass or fail if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

Mark1 = int(input("Enter 1st Mark : "))
Mark2 = int(input("Enter 2dn Mark : "))
Mark3 = int(input("Enter 3rd Mark : "))

per = (Mark1+Mark2+Mark3)/3


if(per > 44) :
    if(Mark1 < 33) : 
        print("You are failed because of you get less than 33 marks in subject")
    elif(Mark2 < 33) :
        print("You are failed because of you get less than 33 marks in subject")
    elif(Mark3 < 33) :
        print("You are failed because of you get less than 33 marks in subject")
    else :
        print("You are passed")
else : 
    print("You are failed")