import random

names_string = input("Enter the names of persons sitting at the table: ")
names_list = names_string.split(", ")

x = len(names_list) - 1

number = random.randint(0,x)
print(names_list)
print(f"{names_list[number]} is going to buy the meal today!")