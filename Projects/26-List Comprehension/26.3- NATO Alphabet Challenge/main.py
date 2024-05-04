import pandas

# TODO 1. Create a dictionary in this format:
alphabet_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_code = {row.letter: row.code for (index, row) in alphabet_dataframe.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word to generate phonetic code: ").upper()
output = [phonetic_code[letter] for letter in user_word]
print(output)
