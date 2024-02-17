"""We will look at inheritance in this chapter, classes can be structured hierarchically, in an is-a relationship also called a parent child relationship."""

class Cycles:
    def set_as_assembled(self,is_assembled):
        self.is_assembled = is_assembled
    
    def get_wheel_count(self):
        return self.wheel_count
    
    def who_am_i(self):
        return "I am the original function"
    
# Creating a class named monocycle that inherits from the Cycles class.
class Monocycle(Cycles):
    """Override the parent function with a similar function that behaves differently."""    
    def who_am_i(self): # We created a new class monocycle that inherits from the class Cycles but we have overridden the function from our parent class by naming the same function but the content are different. 
        return "I am overriding the parent function "
    wheel_count = 1

# Another class that inherits from the Cycles class.
class Bicycle(Cycles):
    wheel_count = 2

# Another class that inherits from the Cycles class.
class Tricycle(Cycles):
    wheel_count = 3


# Creating an object of the Monocycle class.
monocycle = Monocycle()
print(f"\nNumber of wheels in a bicycle: {monocycle.get_wheel_count()}")

bicycle = Bicycle()
print(f"\nNumber of wheels in a bicycle: {bicycle.get_wheel_count()}")

tricycles = Tricycle()
print(f"\nNumber of wheels in a Tricycle: {tricycles.get_wheel_count()}")
print()
print(monocycle.who_am_i()) 
print(bicycle.who_am_i())