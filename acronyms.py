#This program generates acronyms from a number of words entered.
words = input("Enter the words or the sentence to output the acronym:\n")
word_by_word = words.split()
print(word_by_word)

acronym = ""
for i in word_by_word:
    acronym += i[0]

print("The acronym of '{}' is '{}'".format(words,acronym))