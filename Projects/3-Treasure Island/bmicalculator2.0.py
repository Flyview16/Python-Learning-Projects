print("BMI Calculator")

#Take input
height = float(input("Enter your height in m: ") )
weight = int(input("Enter your weight in kg: ") )

#Calculate bmi = weight/heihgt^2
bmi = round(weight / height**2, 2)

#Comments
if bmi < 18.5:
    print(f"Your Body Mass Index is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your Body Mass Index is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your Body Mass Index is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your Body Mass Index is {bmi}, you are obese.")
else:
    print(f"Your Body Mass Index is {bmi}, you are clinically obese.")