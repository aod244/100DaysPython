while True:
    year = int(input("Which year do you want to check? "))

    if year % 4 == 0 :
        if year % 400 == 0:
            print(f"Year {year} is leap year.")
        elif year % 100 == 0:
            print(f"Year {year} is not leap year.")
        else:
            print(f"Year {year} is leap year.")
    else:
        print(f"Year {year} is not leap year.")
 