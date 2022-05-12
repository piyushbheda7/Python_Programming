# Write a python function that converts inches to cms.

def InchesToCms(inch):
    return (inch * 2.54)

n = int(input("Enter the Length in Inches :"))

print(f"The Length in Cms is {InchesToCms(n)}")