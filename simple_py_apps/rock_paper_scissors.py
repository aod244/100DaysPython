import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
while True:
    player_choose = input("What do You choose? Type 0 for Rock, 1 for Paper or 2 for Scisssors\n")
    player_choose = int(player_choose)
    computer_choose = random.randint(0,2)

    choose = [rock,paper,scissors]

    if choose[0] == choose[player_choose] and choose[1] == choose[computer_choose]:
        print(f"Computer picked {choose[computer_choose]} and Player picked {choose[player_choose]}, Paper beats Rock Computer wins!")
    elif choose[0] == choose[player_choose] and choose[2] == choose[computer_choose]:
        print(f"Computer picked {choose[computer_choose]} and Player picked {choose[player_choose]}, Rock beats Scissors Player wins!")
    elif choose[1] == choose[player_choose] and choose[0] == choose[computer_choose]:
        print(f"Computer picked {choose[computer_choose]} and Player picked {choose[player_choose]}, Paper beats Rock Player wins!")
    elif choose[1] == choose[player_choose] and choose[2] == choose[computer_choose]:
        print(f"Computer picked {choose[computer_choose]} and Player picked {choose[player_choose]}, Scissors beats Paper Computer wins!")
    elif choose[2] == choose[player_choose] and choose[0] == choose[computer_choose]:
        print(f"Computer picked {choose[computer_choose]} and Player picked {choose[player_choose]}, Rock beats Scissors Computer wins!")
    elif choose[2] == choose[player_choose] and choose[1] == choose[computer_choose]:
        print(f"Computer picked {choose[computer_choose]} and Player picked {choose[player_choose]}, Scissors beats Paper Player wins!")
    elif choose[player_choose] == choose[computer_choose]:
        print(f"Computer picked {choose[computer_choose]} and Player picked {choose[player_choose]} so it's a draw.")
