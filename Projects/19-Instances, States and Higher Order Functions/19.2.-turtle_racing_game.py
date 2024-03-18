from turtle import Turtle, Screen
import random

screen = Screen()
# Set custom screen size
screen.setup(width=500, height=400)
race_on = False

# Take user input with turtle
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: \n"
                                                          "(red, orange, yellow, green, blue, purple,indigo)")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "indigo"]
y_positions = [-70, -40, -10, 20, 50, 80, 110]
all_turtles = []

# Create objects for each color in colors
for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y= y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    race_on = True

# Move turtles and determine who wins the race
while race_on:
    for turtle in all_turtles:
        # Winner reaches 230 on x-coordinate
        if turtle.xcor() > 230:
            race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You win. The {winning_turtle} turtle wong the race.")
            else:
                print(f"You lose. The {winning_turtle} turtle wong the race.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)









screen.exitonclick()