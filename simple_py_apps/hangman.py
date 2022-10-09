from operator import truediv
import random

word_list = ["aardvark", "baboon", "camel"]
choosen_word = random.choice(word_list)
blank_word = "_" * len(choosen_word)
print(choosen_word)
guess = input("Choose a letter: ").lower()
display = []
num_of_lives = 5

for letter in choosen_word:
    if guess == letter:
        display.append(guess)     
    else:
        display.append("_")
        num_of_lives =- num_of_lives
print(display)
i = 0
while i < len(display) and display[i] == "_":
    print("True")