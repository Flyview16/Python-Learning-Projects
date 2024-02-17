#Your life in weeks if you lived to 90
print("Your Life in Weeks.")

age = 90 - int(input("What is your current age: "))

#Calculate days, weeks and months

days = age * 365
weeks = age * 52
months = age * 12

#Output using f-strings
message = f"You have {days} days, {weeks} weeks and {months} months left."
print(message)