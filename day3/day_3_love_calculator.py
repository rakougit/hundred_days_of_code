words_to_count_1 = "true"
words_to_count_2 = "love"
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
merged_name_lower_case = (name1 + name2).lower()
count_true = 0
count_love = 0
your_score = 0
for word in words_to_count_1:
    count_true += merged_name_lower_case.count(word)
your_score += count_true * 10
for word in words_to_count_2:
    count_love += merged_name_lower_case.count(word)
your_score += count_love
if your_score < 10 or your_score > 90:
    print(f"Your socre is {your_score}, you go together like coke and mentos.")
elif your_score > 40 and your_score < 50:
    print(f"Your score is {your_score}, you are alright together.")
else :
    print(f"Your score is {your_score}.")