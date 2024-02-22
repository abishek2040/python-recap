# Polymorphism is the ability of an object to take on many forms. In OOP, polymorphism is achieved through inheritance.
# Polymorphism is a concept that allows objects of different classes to be treated as objects of a common class.
# Here's an example of polymorphism in Python:


class Pet:
    def sound(self):
        pass # Pass is called a null statement in python and nothing happens when python encounters it. 

# IS-A pet
class Cat(Pet): # New class Cat that inherits from the Pet class. 
    def sound(self):
        print("Meow")

# IS-A Pet
class Dog(Pet): # New class Dog that inherits from the Pet class.
    def sound(self):
        print("Bark")

# Function getSound receives a pet as a parameter, but we are not specifying what kind of pet. Polymorphism is used to resolve this. 

def getSound(pet: Pet):
    return pet.sound()

getSound(Cat()) 
getSound(Dog())
# In this example, the getSound function takes a Pet object as a parameter.