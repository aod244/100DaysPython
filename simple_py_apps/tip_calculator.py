print ("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

pay_per_person = round((bill+((bill*tip)/100))/people , 2)

print(f"Each person should pay: {pay_per_person} $")