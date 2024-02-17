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

print()
print("We see an example of another class: ")

# The fund class

class Funds:

    total_expenses = 0
    total = 0
    # Added a variable to hold any error messages we may encounter.
    error = ""

    # Constructor, we populate it with the total amount available when we construct the object.
 
    def __init__(self, total):
        """This is the constructor, we populate it with the total amount available when we construct the object. """
        self.total = total
    
    def set_expense(self, expense):
        """Stores the money we have spend"""
        if self.get_funds_left() > expense:
            self.total_expenses += expense
            return True
        self.error = "Not enough funds"
        return False
    
    def get_funds_left(self):
        return self.total - self.total_expenses
    
    def get_error(self):
        return self.error
    
fund = Funds(10)
fund.set_expense(10)
fund.set_expense(20)

# prints the amount left to the screen 
amount_left =fund.get_funds_left()
print(f"Amount left: {amount_left}")