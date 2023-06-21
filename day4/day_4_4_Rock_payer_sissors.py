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
min = 0
max = 2

Your_chose = input(
    "What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
Your_chose = int(Your_chose)
Computer_chose = random.randint(min, max)

# Rock_Paper_Sissors_Dictionary = {rock: 0, paper: 1, scissors: 2}

if Your_chose == 0:
    print(rock)
elif Your_chose == 1:
    print(paper)
elif Your_chose == 2:
    print(scissors)

print("computer's choice:")

if Computer_chose == 0:
    print(rock)
elif Computer_chose == 1:
    print(paper)
elif Computer_chose == 2:
    print(scissors)

reslut = Your_chose - Computer_chose
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
