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

game_image = [rock, paper, scissors]

min = 0
max = 2

Your_choice = input(
    "What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
Your_choice = int(Your_choice)
Computer_chose = random.randint(min, max)

if Your_choice >= 0 and Your_choice < 3:
    print(f"Your choice is :{game_image[Your_choice]}\n")
else:
    print("You input a wrong number\n")

print(f"computer's choice is : {game_image[Computer_chose]}\n")

reslut = Your_choice - Computer_chose

if reslut == 0:
    print("Draw")
elif reslut == 1:
    print("You win")
elif reslut == -1:
    print("You lose")
elif reslut == 2:
    print("You lose")
elif reslut == -2:
    print("You win")
else:
    print("You input a wrong number, please try again")
