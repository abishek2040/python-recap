# List Comprehension is a short way of creating a list using a for loop in Python. It is a concise way to create a list in Python.

numbers = [1, 2, 3, 4, 5]

def multiply(amount):
    return amount * 10

# Here, we use list comprehension to create a list of numbers and call the list "result"

result = [multiply(number) for number in numbers]
print(f"Here's the new list of numbers: {result}")