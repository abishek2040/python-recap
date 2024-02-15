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



# Variable number of arguments in a function. Sometimes we don't know how many arguments a function will take, so we can use variable number of arguments.
# In Python, we can use *args to pass variable number of arguments to a function.
# Here's an example:

def add(*numbers):
    """A function that takes variable number of arguments and returns their sum."""
    sum = 0 
    for number in numbers:
        sum += number
    
    print(f"The sum of the numbers is: {sum}")

add(1, 2, 3, 4, 5)
add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)



# The above example shows variable arguments, which are passed to a function as a tuple.
# Here's an example of Keyword Arguments in Python:
# keyword arguments are used to pass arguments to a function in a key-value pair. In a keyword argument the order of argument does not matter. 
# As long as they are passed in the correct order, the function will work.
# Here's an example:

def person(name, age):
    return f"\nHello {name}, you are {age} years old."

details = person(age=22, name="Abishek")
print(details)




# Summary for the functions chapter: 

# A function is a block of code that performs a specific task. Which can be reused by calling the function. 

# We should create a single function for one task, which helps us to manage our code much efficiently. 

# Should a function return or print: The answer depends on the task and the obbjective of the function, if the function just wants to display the result on the screen, 
# then it should print the result and if it needs to store the result in a variable, then it should return the result.

# Variable number of arguments in a function: We can use *args to pass variable number of arguments to a function.

# Keywords arguments can be used to pass arguments to a function in a key-value pair, in which the order of the arguments doesn't matter as long as they are passed in a key-value pair. 

# Parameter Type Hinting: We can use type hinting to specify the type of the parameter in a function. for example, if we are expecting an argument for age of a person, we'd always like that 
# value to be an integer. Thus, we can use type hinting to specify the type of the parameter like this: def person(name: str, age: int) -> str:

# Default parameter values: We can specify default values for parameters in a function, in situations where we are unsure if we'll receive a value or not. 


