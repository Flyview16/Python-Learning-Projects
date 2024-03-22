from turtle import Turtle, Screen
from snake import Snake
import time


# Setting up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)    # turn off animation

# Creating snake body
snake = Snake()

# Set listener to monitor keystrokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Move snake
game_on = True
while game_on:
    screen.update()     # update the screen
    time.sleep(0.1)
    snake.move()


















screen.exitonclick()