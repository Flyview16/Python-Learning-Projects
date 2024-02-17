print("BMI Calculator")

#Take input
height = float(input("Enter your height in m: ") )
weight = int(input("Enter your weight in kg: ") )

#Calculate bmi = weight/heihgt^2
bmi = weight / height**2

#Output, round up bmi to 2 dp
print("Your Body Mass Index is: " + str(round(bmi,2) ) )
