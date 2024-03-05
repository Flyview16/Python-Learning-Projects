import random
import os
from art import logo

#List of cards to deal
def deal_cards():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#Calculate score by adding sum of list items, takes list of cards as input
def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards"""
    #Check for a blackjack, a hand with only 2 cards (ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    #Check for an 11 (ace) and replace with 1 if score is already over 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Compare the scores and determine the winner
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw🙃"
    elif computer_score == 0:
        return "You lose, opponent has Blackjack😱"
    elif user_score  == 0:
        return "Win with a Blackjack😎"
    elif user_score > 21:
        return "You went over. You lose😭"
    elif computer_score > 21:
        return "Opponent went over. You win😁"
    elif user_score > computer_score:
        return "You win😄"
    else:
        return "You lose😤"

#Play Blackjack
def play_game():
    print(logo)
    # Deal the computer and user 2 cards each using deal_card()
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    
   
    #User play
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card : {computer_cards[0]}")


        #Game ends if either player has blackjack (0) or user score above 21
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            deal_user = input("Type 'y' to get another card, type 'n' to pass: ")
            if deal_user == 'y':
                user_cards.append(deal_cards())
            else:
                game_over = True

    #Computer play, to continue drawing cards as long as score is less than 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a new game of Blackjack? Type 'y' or 'n': ") == 'y':
    os.system('cls')
    play_game()
