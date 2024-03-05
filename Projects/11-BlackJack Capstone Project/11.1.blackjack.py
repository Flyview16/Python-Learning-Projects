import random

#List of cards to deal
def deal_cards():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#Calculate score by adding sum of list items, takes list of cards as input
def calculate_score(cards):
    return sum(cards)

# Deal the computer and user 2 cards each using deal_card()
user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

