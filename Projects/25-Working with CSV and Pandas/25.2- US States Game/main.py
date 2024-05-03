import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=800)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read csv file
data = pandas.read_csv("50_states.csv")

# Extract states
states = data.state.to_list()

guessed_state = []


while len(guessed_state) < 50:
    # Take user input
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 Correct States", prompt="What is the name of a "
                                                                                            "state?").title()

    # Check if answer is part of states
    if answer_state in states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)

screen.exitonclick()
