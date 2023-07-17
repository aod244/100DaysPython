import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.pensize(1)
tim.speed("fastest")
turtle.colormode(255)

# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#
#
# for shape_side_n in range(3,11):
#     draw_shape(shape_side_n)
#
# choices = [0, 90, 180, 270]
#
# for _ in range(200):
#     random_color_tuple = random_color()
#     tim.forward(25)
#     tim.right(random.choice(choices))
#     tim.pencolor(random_color_tuple)
#     tim.color(random_color_tuple)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)
        tim.color(random_color())


draw_spirograph(1)


screen = turtle.Screen()
screen.exitonclick()
