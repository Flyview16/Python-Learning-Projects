from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
screen.onkeypress(r_paddle.go_up, key="Up")
screen.onkeypress(r_paddle.go_down, key="Down")
screen.onkeypress(l_paddle.go_up, key="w")
screen.onkeypress(l_paddle.go_down, key="s")

# Create ball object
ball = Ball()

# Create scoreboard object
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor() > 288 or ball.ycor() < -288:
        ball.bounce_y()

    # Detect collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if right paddle misses a ball
    if ball.xcor() > 350:
        ball.reset()
        score.l_point()

    # Detect if left paddle misses a ball
    if ball.xcor() < -350:
        ball.reset()
        score.r_point()

screen.exitonclick()
