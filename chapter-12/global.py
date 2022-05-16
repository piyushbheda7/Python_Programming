a = 9 
def func():
    global a # this will change in the global variable
    a = 3 
    print(a)
    a = 900
    print(a)

print(a)
func()
print(a)