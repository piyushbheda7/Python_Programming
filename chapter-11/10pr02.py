# Create a class of pets from a class Animals and further create class Dog from Pets. Add a method bark to class Dog.

class animal:
    name = "animals"

class pets(animal):
    names = "pets"

class Dog(pets):
    def bark(self):
        print("Dogs are barking bhau bhau........")

dg = Dog()
print(f"Dogs are {dg.names}")
dg.bark()
