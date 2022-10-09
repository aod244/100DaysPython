from itertools import count
import string
from time import time
from unicodedata import name


print("Welcome to the Love Calculator!")
name1 = (input("What is Your name? \n")).lower()
name2 = (input("What is Their name? \n")).lower()

name_sum = name1 + name2

t = name_sum.count("t")
r = name_sum.count("r")
u = name_sum.count("u")
e = name_sum.count("e")

l = name_sum.count("l")
o = name_sum.count("o")
v = name_sum.count("v")
e = name_sum.count("e")

sum_true = t+r+u+e
sum_love = l+o+v+e

score = str(sum_true) + str(sum_love)
score = int(score)
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
