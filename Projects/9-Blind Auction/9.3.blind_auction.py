import os
from art import logo

print(logo)
blind_auction = {}
continue_bid = True

def find_highest_bidder(bidding_record):
    winner_amount = 0
    for bid in bidding_record:
        if bidding_record[bid] > winner_amount:
            winner_amount = blind_auction[bid]
            winner = bid

    #Output
    print(f"\nThe winner is {winner} with a bid of ${winner_amount}")

#Start
print("Welcome to the secret auction program.")

#Continue bid till there are no more bidders
while continue_bid:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    blind_auction[name] = price
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n")

    if other_bidders == 'yes':
        #Clear screen for next bidder
        os.system('cls')
    elif other_bidders == 'no':
        continue_bid = False
        find_highest_bidder(blind_auction)
    else:
        print("Please choose either 'yes' or 'no'.")

