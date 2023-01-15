"""Program to count how many times each letter appears in a string"""

string = input("Please input a string: ")
string = (string.replace(" ", "")).lower()

letters = {}

for letter in string:
    if letter in letters:
        letters[letter] += 1
    else:
        letters[letter] = 1

print(letters)
