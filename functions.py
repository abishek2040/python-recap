import datetime
# Functions are reusable blocks of code, which are used to perform a specific task, and once defined can be reused in multiple places by using their name, which is known as 
# calling a function. 
# A function can take zero or more arguments, which are known as parameters.

# A function should always be created for one goal, which means, if you have a task to add 2 numbers a single function should be made. 

# Here's an example of a function:

def details(name, surname):
    """A function that takes 2 args, name and surname and returns it in a well formatted manner."""
    return f"Hello my name is: {name}, {surname}"

info = details("John", "Doe")
print(info)

print()
print()
# Let's have a look at a function bit more complex. 

# we've imported the datetime module, which is used to work with dates and times.

def calc_age(birth_year) -> int:
    """A function that takes a birth year and returns the age of the person."""
    current_year = datetime.datetime.now().year
    return current_year - birth_year 

age = calc_age(2000)
print(age)

print("Here we have another example: \n")

def person(name, money):
    """A function that takes 2 args, name and money and returns the person's name and money."""
    coffee_cost = 4
    if money >= coffee_cost:
        print(f"Hello {name}, you can buy a coffee.")
    else:
        print(f"Hello {name}, you can't buy a coffee.")

person("Abishek", 4)
