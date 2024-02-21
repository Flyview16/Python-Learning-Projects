import random

word_list = ["aardvark", "baboon", "camel"]

#Randomly choose a word from the word_list 
chosen_word = random.choice(word_list)
display = []
for num in chosen_word:
    display.append("_")
print(display)

end_of_game = False

while not end_of_game:

    #Ask the user to guess a letter
    guess = input("Guess a letter: ").lower()

    # Check if the letter the user guessed is one of the letters in the chosen_word and replace in display.
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)
    
    # Check if there are no more blanks in display and end game
    if "_" not in display:
        end_of_game = True
        print("You win")
