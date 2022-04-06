import random as r

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
game_images = [rock, paper, scissors]

# people choice
user_choice = int(input("What do you choose? Print 0 for Rock, 1 for Paper and 2 for Scissors... "))
if 0 < user_choice <= 2:
    print(game_images[user_choice])
else:
    print("You type an invalid number")
    exit()

# computer choice
computer_choice = r.randint(0, 2)
print(game_images[computer_choice])

# displaying the result
result = [user_choice, computer_choice]
if user_choice == computer_choice:
    print("It's a draw")
elif result == [0, 2] or result == [1, 0] or result == [2, 1]:
    print("You WIN!")
elif result == [0, 1] or result == [1, 2] or result == [2, 0]:
    print("You LOSE!")
else:
    print("ERROR")
