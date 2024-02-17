print ("Even or Odd Checker")

number = int(input("Which number do you want to check out? "))

#Check (using modulo)
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")