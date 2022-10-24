print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age > 18:
        bill = 12
        print(f"Adult tickets are ${bill}.")
    elif age >= 12:
        bill = 7
        print(f"Youth tickets are ${bill}.")
    elif age >= 45 and age <= 55:
        bill = 0
        print(f"Everything is going to be ok. Have a free ride on us") 
    else :
        print(f"Child tickets are ${bill}.")

    photo_flag = input("Do you want a photo taken ? Y or N. ")
    if photo_flag == "Y":
        bill += 3
    print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")