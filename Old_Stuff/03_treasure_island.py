print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."'` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_choice = input("\nYou are on the crossroad. Which path do you prefer to choose? Left/Right ").lower()
if first_choice == "left":
    print("Good choice, traveller!")
    second_choice = input("\nYou see huge poisonous lake in front of you. Will you try to swim or wait? Swim/Wait ").lower()
    if second_choice == "wait":
        print("Giant bird have taken you and gave you a lift. Interesting.\n")
        third_choice = input(
            "Then, three magic doors appeared in front of you. Red, Blue and Yellow. Which you gonna choose?").lower()
        if third_choice == "red":
            print("There was a lot of fire behind that door. You've burned to death.\nGame Over.")
        elif third_choice == "yellow":
            print("Behind the door were treasures and cute princess.\nYou've won! Congratulations, mate!")
        elif third_choice == "blue":
            print("There were beast behind that door. You were eaten. Poor you.\nGame over...")
        else:
            print("Don't be silly. You've been murdered by your stupidity\nGame over!")
    else:
        print("You've died miserably. You really bad at decisions! Game over.")
else:
    print("You have fallen into a hole. Game over!")



