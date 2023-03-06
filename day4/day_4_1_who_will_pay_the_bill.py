#TODO: pick up a person randomly in the list to ask him/her to pay the meal Angela, Ben, Jenny, Michael, Chole
#TODO: Example Output : Michael is going to buy the meal today!

import random

names_string = input("Give me everybody's name,s, seperated by a comma.")
names = names_string.split(",")

min = 0
max = len(names)

name_index = random.randint(min, max)

guy_to_pay = names[name_index]
print(f"{guy_to_pay} will pay the bill")