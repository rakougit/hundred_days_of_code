print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print('Welcome to Treasure Island.\nYou mission is to find the treasure.')
choice_1 = input('You\'re at a crossroad.\nWhere do you want to go? Type "left" or "right".\n').lower()
if choice_1 == "left":
    choice_2 = input('You\'ve come to a lake.\nThere is an island in the middle of the lake.\nType "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice_2 == "wait":
        choice_3 = input('You arrived at athe island unharmed.\nThere is a house with 3 doors.\nOne "red", one "yellow" and one "blue". Which colour do you choose ?\n').lower()
        if choice_3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice_3 == "yellow":
            print("Congratulations, you found the treasues. You Win.")
        elif choice_3 == "blue":
            print("You entered a room of beast. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game over")

# if not life_flag:
#     print("You fell into a hole. Game Over.")
#     exit()

# life_flag = 0
# User_input = input("Will you swim or wait ?").lower()
# if User_input == "wait":
#     life_flag = 1
# if not life_flag:
#     print("Game over")
#     exit()

# life_flag = 0
# User_input = input("Which door will you choose ? Blue, Red or Yellow ?").lower()
# if User_input == "yellow":
#     life_flag = 1
#     print("You win !")
# if not life_flag:
#     print("Game over")
#     exit()