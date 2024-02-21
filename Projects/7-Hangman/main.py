import random
import hangman_words

from hangman_art import logo, stages

#Display hangman logo
print(logo)

end_of_game = False
lives = 6

#Randomly choose a word from the word_list 
chosen_word = random.choice(hangman_words.word_list)
display = []
for num in chosen_word:
    display.append("_")


while not end_of_game:

    #Ask the user to guess a letter
    guess = input("Guess a letter: ").lower()

    #Check if guessed letter has already been guessed
    if guess in display:
        print(f"You've already guessed {guess}")
    # Check if the letter the user guessed is one of the letters in the chosen_word and replace in display.
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if guess is not in chosen_word
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    
    print(f"{''.join(display)}")

    # Check if user got all letters
    if "_" not in display:
        end_of_game = True
        print("You win")

    # Print ASCII art for stages based on lives
    print(stages[lives])