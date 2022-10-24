print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
add_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You might have a wrong input for the size")

if size == "S" and add_pepperoni == "Y":
    bill += 2
elif (size == "M" or size == "L") & add_pepperoni == "Y":
    bill += 3
else:
    print("You might have a wrong input for the pepperoni option")

if add_cheese == "Y":
    bill += 1
else:
    print("You might have a wrong input for the cheese option")
print(f"Your bill is {bill}")