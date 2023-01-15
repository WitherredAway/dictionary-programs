"""A game to guess a word from its definition"""

import random
import time


dictionary = {
    "programming": "the process or activity of writing computer programs.",
    "python": "a general-purpose, interpreted, high-level programming language popularly used for website development, data analytics and automation.",
    "computer science": "the study of the principles and use of computers.",
    "turtle": "a large marine reptile with a bony or leathery shell and flippers, coming ashore annually on sandy beaches to lay eggs.",
    "cat": "a small domesticated carnivorous mammal with soft fur, a short snout, and retractable claws. It is widely kept as a pet or for catching mice, and many breeds have been developed."
}

points = 0
while True:
    time.sleep(0.5)
    word, definition = random.choice(list(dictionary.items()))

    print()
    guess = input(f"{definition}\nGuess the word: ")

    if guess.lower() == word:
        points += 1
        print(f"Correct! +1 Point (Total {points})")
    else:
        print(f"Game over! Total score: {points}")
        break