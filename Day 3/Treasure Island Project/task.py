print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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

firstUserInput = input("You\'re at cross roads. Which way do you go?\n"
                       "left or right\n")

if not firstUserInput.lower() == "left":
    print("Fall into a hole.\n Game Over.")
    exit()

secondUserInput = input("You\'ve come to a lake.\n"
                        "What do oyu do? "
                        "swim or wait\n")

if not secondUserInput.lower() == "wait":
    print("Attacked by trout.\nGame Over.")
    exit()

thirdUserInput = input("Which door do you go through?\n Yellow, Blue or Red")

if thirdUserInput.lower() == "blue":
    print("Eaten by beasts.\nGame Over.")
    exit()
elif thirdUserInput.lower() == "Red":
    print("Burned by fire.\n Game Over.")
    exit()
elif thirdUserInput.lower() == "yellow":
    print("You Win!")
else:
    print("Game Over.")
    exit()