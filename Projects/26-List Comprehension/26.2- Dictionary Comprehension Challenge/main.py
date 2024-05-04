# Challenge 1: count the number of letters in each word of the sentence
# convert string to list of words
sentence = "What is the Airspeed Velocity of an Unladen Swallow?".split()

# count number of letters and put in dictionary
result = {word: len(word) for word in sentence}
print(result)


# Challenge 2: convert dictionary of temperatures in Celsius to Fahrenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)


