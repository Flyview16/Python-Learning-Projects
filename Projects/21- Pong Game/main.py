from turtle import Turtle, Screen
from paddle import Paddle


# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # turn off animation

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Set up paddle key controls
screen.listen()
screen.onkey(r_paddle.go_up, key="Up")
screen.onkey(r_paddle.go_down, key="Down")
screen.onkey(l_paddle.go_up, key="w")
screen.onkey(l_paddle.go_down, key="s")


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
