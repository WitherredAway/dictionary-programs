"""Program to view definition of a word from a dictionary of definitions"""

dictionary = {
    "programming": "the process or activity of writing computer programs.",
    "python": "Python is a general-purpose, interpreted, high-level programming language popularly used for website development, data analytics and automation.",
    "computer science": "the study of the principles and use of computers.",
    "turtle": "a large marine reptile with a bony or leathery shell and flippers, coming ashore annually on sandy beaches to lay eggs.",
    "cat": "a small domesticated carnivorous mammal with soft fur, a short snout, and retractable claws. It is widely kept as a pet or for catching mice, and many breeds have been developed."
}

word = input("See definition of a word: ")
print(dictionary.get(word) or "Word not found.")