import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


# # Draw a square with Tim the turtle
# for i in range (4):
#     tim.forward(100)
#     tim.left(90)

# # Draw short dashes
# for i in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Draw shapes from triangle to decagon
# for sides in range(3, 11):
#     tim.color(random.choice(colors))
#     for i in range(sides):
#         tim.forward(100)
#         tim.right(360 / sides)


# Draw random walks
# moves = [0, 90, 180, 270]
# tim.pensize(10)
#
#
# for i in range(300):
#     tim.color(random_color())
#     tim.forward(20)
#     tim.setheading(random.choice(moves))


# Draw a spirograph
draw_spirograph(5)

screen = Screen()
screen.exitonclick()
