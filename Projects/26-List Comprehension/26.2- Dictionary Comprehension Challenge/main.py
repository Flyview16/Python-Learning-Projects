# count the number of letters in each word of the sentence
# convert string to list of words
sentence = "What is the Airspeed Velocity of an Unladen Swallow?".split()

# count number of letters and put in dictionary
result = {word: len(word) for word in sentence}
print(result)


