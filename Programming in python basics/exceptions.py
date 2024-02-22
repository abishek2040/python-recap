# Exceptions are the errors that occur during the execution of a program.
# Exception simply means that something went wrong while the program was running.
# There are many types of exceptions in python, exceptions that are thrown by python are not very readable and cannot be understood by all.
# So, we can modify the exceptions into a user friendly messages, to let the user know what went wrong.

# Here's an example of a user-friendly exception:
try:    
    number = 10/0
except ZeroDivisionError:
    print("You cannot divide a number by zero")
# This is a simple example of a user-friendly exception, without the except block, python would just print zeroDivisionError but we can print a more user friendly message. 
    

