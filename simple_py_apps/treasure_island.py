print("Welcome to Treasure Island. \nYour mision is to find the treasure.")
way = input("Which way You want to go? left or right?\n")
if way == "right":
    print("Game over!")
else:
    print("You came to a river You want to wait for a boat or swim across?")
    decision = input()
    if decision == "swim":
        print("Game over!")
    else:
        print("You swim across the river with a boat and You came to the treasure island.")
        doors = input("You see three doors each one has differen colour, which one You choose? red, blue or yellow?\n")
        if doors == "red" or doors == "blue":
            print("Game over!")
        elif doors == "yellow":
            print("You win! GZ!")
        