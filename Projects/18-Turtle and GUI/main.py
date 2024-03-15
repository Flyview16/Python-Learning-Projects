from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

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
moves = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fast")

for i in range(300):
    tim.color(random.choice(colors))
    tim.forward(20)
    tim.setheading(random.choice(moves))













screen = Screen()
screen.exitonclick()