# There's some more elements to the loops in python that just the for loop and while loop. The other important things to look for is how we can use nested loops, which is not 
# always ideal, but is sometimes required by your program. Also, we have the continue and the break statements, which are used to control the flow of the loop, and are important 
# aspect in loops in python and also in many other languages. 

# Here's an example of a nested loop:

people = [{"name": "ron", "position": "Manager"}, {"name": "bob", "position": "CEO"}, {"name": "sue", "position": "CFO"}]
for i in people:
    for k,v in i.items():
        print (k, ":",v)

print()
# Here's an example that uses continue statement in python: 
for person in people:
    for details_key, details_value in person.items():
        if person["position"] == "CEO":
            continue
        print (details_value)

# Here's an example that uses break statement in python:
print()

for person in people:
    for details_key, details_value in person.items():
        if person["position"] == "CEO":
            break
        print (details_value)