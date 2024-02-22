import math

#Function definition
def paint_calc(height, width, cover):
    area = height * width
    number_of_cans = math.ceil(area / cover)           #math.ceil used to round up numbers to ceiling
    print(f"You'll need {number_of_cans} cans of paint")

#User input
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall:"))
coverage = 5

#Function Call
paint_calc(height = test_h, width = test_w, cover = coverage)