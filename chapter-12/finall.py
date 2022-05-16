def function():
    try:
        a = int(input("Enter a number : "))
        b =int(input("Enter another number :"))
        print(a/b)
    except Exception as e:
        print(f"This Problem Occured : {e}")
    else:
        print("Try was successful")
    finally:
        print("This will always be printed")

print(__name__) # it will print like __name__ but if it is imported into another file then it will print the file name as finall


if __name__ =='__main__': # -> if it is not added then it can be imported as module in another file if added it will nothing to do 
    function()
    print('main')