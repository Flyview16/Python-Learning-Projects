import random

print("Who's paying?")

names_string = input("Give me everybody's name separated by a comma. ")
names = names_string.split(", ")
payer = random.randint(0,len(names)-1)

print(f"{names[payer]} is going to buy the meal today")