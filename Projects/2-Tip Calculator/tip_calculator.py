print("Welcome to the tip calculator.")

#Take bill and tip percent
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

#Calculate tip
tip_amount = bill * (tip  / 100)
total_bill = round(bill + tip_amount, 2)
each_person_pays = total_bill / people
final_amount = "{:.2f}".format(each_person_pays)

#Output
print(f"The total bill is: ${total_bill}")
print(f"Each person pays ${final_amount}")