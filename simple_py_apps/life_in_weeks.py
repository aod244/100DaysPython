age = int(input("What is Your current age? "))

age_in_months = age * 12
age_in_weeks = age * 52
age_in_days = age * 365

age_left_months = (90*12) - age_in_months
age_left_weeks = (90*52) - age_in_weeks
age_left_days = (90*365) - age_in_days

print(f"You have {age_left_days} days, {age_left_weeks} weeks and {age_left_months} months left.")