import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=1000, height=800)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

def create_turtles():
    x = -400
    y = -300
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x, y)
        all_turtles.append(new_turtle)
        y += 100
    return all_turtles


turtles = create_turtles()
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 480:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You've won! The {wining_color} turtle is the winner! ")
            else:
                print(f"You've lost! The {wining_color} turtle is the winner! ")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
