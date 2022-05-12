# Write a python program using the function to convert Celsius to Fahrenheit.

def CelToFah(c):
    return ((c * (9/5)) + 32)

temp = int(input("Enter a Temperature : "))

print(f"The Fahrenheit value of {temp} is {CelToFah(temp)}")

