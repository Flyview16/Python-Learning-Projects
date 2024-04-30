from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x_pos = self.xcor() + self.x_move
        new_y_pos = self.ycor() + self.y_move
        self.goto(new_x_pos, new_y_pos)

    def bounce_y(self):
        # Reverse direction of ball
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.75  # increase ball speed after it hit paddle

    def reset(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_x()


