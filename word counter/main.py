"""Program to count how many times each word appears in a string"""

sentence = input("Please input a sentence: ")
words = sentence.split(" ")

words_dict = {}

for word in words:
    word = word.lower()
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

print(words_dict)
