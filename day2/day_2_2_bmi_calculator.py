weight = input("Please type your weight = ")
height = input("Please type your height = ")

# bmi = int(int(weight) / int(height) ** 2)
bmi = int(weight) / float(height) ** 2
print(f"your bmi is {int(bmi)}.")