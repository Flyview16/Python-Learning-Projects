from art import logo
from art import vs
import random
from game_data import data

score = 0
game_over = False
option1 = random.choice(data)
option2 = random.choice(data)

while not game_over:
    #print(logo)

    print(f"Compare A: {option1['name']}, a {option1['description']}, from {option1['country']} ")
    #print(vs)
    print(f"Against B: {option2['name']}, a {option2['description']}, from {option2['country']}")

    choice = input("Who has more followers? Type 'A' or 'B': ")

    if choice == 'A':
        if option1['follower_count'] >= option2['follower_count']:
            score += 1
            option1 = option2
            option2 = random.choice(data)
        else:
            game_over = True
    elif choice == 'B':
        if option2['follower_count'] >= option1['follower_count']:
            score += 1
            option1 = option2
            option2 = random.choice(data)
        else:
            game_over = True
    else:
        print("Invalid input. Start again.")
        game_over = True
