# Magic methods are the special methods that start and end with double underscores. They are also known as dunder methods.
# Magic methods are used for operator overloading.
# Here's an example of a magic method in Python:

class Member:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Group:
    def __init__(self):
        self.members = []

    def __add__(self, x:Member, y:Member):
        self.members.append(x.name, y.surname)
        print(self.members)


member1 = Member("Abishek", "Phuyal")
member2 = Member("Kumar", "Bhatta")
group = Group() 
group + member1
group + member2
