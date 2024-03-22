from turtle import Turtle, Screen
import time

# Setting up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)    # turn off animation

# Creating snake body
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
game_on = True
for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# Move snake
while game_on:
    screen.update()     # update the screen
    time.sleep(0.1)

    for seg in range(len(segments) - 1, 0, -1):
        new_x = segments[seg - 1].xcor()
        new_y = segments[seg - 1].ycor()
        segments[seg].goto(new_x, new_y)
    segments[0].forward(20)

















screen.exitonclick()