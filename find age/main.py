"""Program that stores name and age of people and allows user to see age of an user"""

people = {"John": 25, "Mary": 32, "Kevin": 40, "Amy": 22}


def search_age(name):
    if name in people:
        return people[name]
    else:
        return "Name not found"


name = input("Enter a name: ")

age = search_age(name)

print("The age of", name, "is", age)
