import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=800)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Take user input
answer_state = screen.textinput(title="Guess the State", prompt="What is the name of a state?").capitalize()

# Read csv file
data = pandas.read_csv("50_states.csv")

# Extract states
states = data.state.to_list()

# Check if answer is part of states
if answer_state in states:
    turtle = turtle.Turtle()
    turtle.penup()
    turtle.hideturtle()
    state_data = data[data.state == answer_state]
    turtle.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
    turtle.write(answer_state)

screen.exitonclick()
