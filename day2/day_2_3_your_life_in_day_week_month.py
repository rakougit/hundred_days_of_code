age = input("what is your current age ")
age_year_int = int(age)
age_month_remaining_int = 12 * (90 - age_year_int)
age_week_remaining_int = 52 * (90 - age_year_int)
age_day_remaining_int = 356 * (90 - age_year_int)
message = f"You have {age_day_remaining_int} days, {age_week_remaining_int} weeks, and {age_month_remaining_int} months left."
print(message)