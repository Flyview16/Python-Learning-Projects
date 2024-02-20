#Adding all even numbers between from 1 to 100
#Using modulo
even_adder1 = 0
for number in range(1,101):
    if number % 2 == 0:
        even_adder1 += number

print(even_adder1)

#Using range step
even_adder2 = 0
for number in range(2,101,2):
    even_adder2 += number

print(even_adder2)
