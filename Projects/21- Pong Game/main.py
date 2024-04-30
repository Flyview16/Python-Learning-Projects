from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time


# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # turn off animation

# Create paddle objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Set up paddle key controls
screen.listen()
screen.onkey(r_paddle.go_up, key="Up")
screen.onkey(r_paddle.go_down, key="Down")
screen.onkey(l_paddle.go_up, key="w")
screen.onkey(l_paddle.go_down, key="s")

# Create ball object
ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    ball.move()

screen.exitonclick()
