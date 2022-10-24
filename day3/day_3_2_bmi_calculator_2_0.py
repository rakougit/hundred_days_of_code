weight = input("Please type your weight in kg = ")
height = input("Please type your height in m = ")

# bmi = int(int(weight) / int(height) ** 2)
bmi = round(int(weight) / float(height) ** 2)

if bmi < 18.5:
    print(f"your bmi is {int(bmi)} they are underweight.")
elif bmi < 25:
    print(f"your bmi is {int(bmi)} they have a normal weight.")
elif bmi < 30:
    print(f"your bmi is {int(bmi)} they are overweight.")
elif bmi < 35:
    print(f"your bmi is {int(bmi)} they are obese.")
else:
    print(f"your bmi is {int(bmi)} they are clinically obese.")