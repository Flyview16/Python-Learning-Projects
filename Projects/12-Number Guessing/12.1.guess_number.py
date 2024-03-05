import random

#Guessing logic
def guessing_game(guessed_number, attempts_left):
     for i in range(attempts_left):
        print (f"You have {attempts_left} remaining attempts to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == guessed_number:
            return f"You go it. The answer was {guessed_number}"
        elif guess > guessed_number:
            print("Too high.\nGuess again")
        elif guess < guessed_number:
            print("Too low.\nGuess again")
        else:
            print("Out of range.Try Again.")
        attempts_left -= 1
        if attempts_left == 0:
            return f"You have run out of guesses. The answer was {guessed_number}"




print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
answer = random.randint(1, 100)
number_of_attempts = 0

#Set difficulty with attempts
if difficulty == 'easy':
    number_of_attempts = 10
elif difficulty == 'hard':
    number_of_attempts = 5

result = guessing_game(answer, number_of_attempts)
print(result)


