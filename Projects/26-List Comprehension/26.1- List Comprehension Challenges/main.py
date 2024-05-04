# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# # Square all numbers in the list using list comprehension
# squared_numbers = [num ** 2 for num in numbers]
#
# # Find all even numbers in the list using list comprehension
# result = [num for num in numbers if num % 2 == 0]
#
# print(squared_numbers)
# print(result)


# List comprehension challenge
# read file 1 and 2
with open("file1.txt") as file1:
    num_list1 = file1.readlines()

with open("file2.txt") as file2:
    num_list2 = file2.readlines()

# Compare to find common items using list comprehension
result = [int(common) for common in num_list1 if common in num_list2]

print(result)
