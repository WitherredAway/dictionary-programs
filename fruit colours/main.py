"""Program to manage a dictionary of colours of fruits"""

# create a dictionary
fruits = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}

# add a new key-value pair to the dictionary
fruits['grape'] = 'purple'

# update the value of an existing key
fruits['banana'] = 'brown'

# remove a key-value pair from the dictionary
del fruits['orange']

# print the entire dictionary
print(fruits)

# print the value of a specific key
print(fruits[input("Enter fruit: ")])