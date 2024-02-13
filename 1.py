# While Loop
number =0
while number < 10 or number * 10 < 50:
    print(number)
    number += 1


# For Loops:
print()
names = ["John", "Jane", "Mary", "Mark"]
for name in names:
    print(name) # This is a simple for loop. 


# For loop - 2 

names = ["John", "Jane", "Mary", "Mark"]
for name in names:
    if name == "Mary":
        print("\nYes, mary is in the list: ")


# Looping through a dictionary: 

personal_details = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "country": "USA", 
    "marital Status": "Married"
}

for k,v in personal_details.items():
    print("\n",k, ":", v) # This is how we use for loop in a dictionary. They are iterated differently from lists, tuples, & strings sue to the fact 
    #that they possess a key. In this case, the key is the variable k and the value is the variable v.

    
        