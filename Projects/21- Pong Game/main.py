from turtle import Turtle, Screen

# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # turn off animation

# Setting up paddle
paddle = Turtle(shape="square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)


def go_up():
    new_y_pos = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y_pos)


def go_down():
    new_y_pos = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y_pos)


# Set up paddle key controls
screen.listen()
screen.onkey(go_up, key="Up")
screen.onkey(go_down, key="Down")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
