from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setting up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # turn off animation

# Creating snake body, food and scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Set listener to monitor keystrokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move snake
game_on = True
while game_on:
    screen.update()  # update the screen
    time.sleep(0.1)
    snake.move()

    # Detect Collision
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

screen.exitonclick()
