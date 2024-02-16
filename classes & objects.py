# On a high level understanding, a class is a blueprint for creating objects. It encloses or encapsulates, behaviors and attributes for objects. 
# Objects are instances of a class. They have their own state and behavior.

# Here is an example of a class:

class Dog():
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color
    
    def bark(self):
        print(f"{self.name} is barking. ")
    
    def run(self):
        print(f"{self.name} is running. ")
    
dog1 = Dog("Max", "Labrador", "Brown")
dog2 = Dog("Buddy", "Poodle", "White")

dog1.bark()
dog1.run()
print()
dog2.bark()
dog2.run()

