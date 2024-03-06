from art import logo, vs
import random
import os
from game_data import data


def format_data(option):
    """Take option data and return printable format"""
    option_name = option['name']
    option_descr = option['description']
    option_country = option['country']
    return f"{option_name}, a {option_descr}, from {option_country}"

def check_answer(choice, a_followers, b_followers):
    """Takes choice and compares followers to see it player got it right."""
    if a_followers > b_followers:
        return choice == "a"
    else:
        return choice == "b"
    

score = 0
game_over = False
option1 = random.choice(data)
option2 = random.choice(data)
if option1 == option2:
    option2 = random.choice(data)

print(logo)

#Make game repeatable
while not game_over:
    print(f"Compare A: {format_data(option1)}")
    print(vs)
    print(f"Against B: {format_data(option2)}")

    #Take player choice
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = option1['follower_count']
    b_follower_count = option2['follower_count']

    #Check if user is right
    is_correct = check_answer(choice, a_follower_count, b_follower_count)

    #Clear screen after each round
    os.system('cls')
    print(logo)

    #Feedback and keeping track of score
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
        option1 = option2
        option2 = random.choice(data)
    else:
        print(f"Sorry you're wrong. Final score: {score}")
        game_over = True