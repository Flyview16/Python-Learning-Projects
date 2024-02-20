import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Rock-Paper-Scissors")
choice1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))

choice2 = random.randint(0,2)

game_images = [rock, paper, scissors]


print(f"You chose:\n {game_images[choice1]}")
print(f"Computer chose:\n {game_images[choice2]}")

#RPS logic, instances where player loses
if choice1 == choice2:
    print("It's a draw")
elif choice1 == 0 and choice2 == 1:
    print("You lose")
elif choice1 == 1 and choice2 == 2:
    print("You lose")
elif choice1 == 2 and choice2 == 0:
    print("You lose")
else:
    print(" You win!!")