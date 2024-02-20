#Print all numbers from 1 to 100, if number is fully divisible by 3, print Fizz, by 5, print Buzz.
#By 3 and 5, print FizzBuzz

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)