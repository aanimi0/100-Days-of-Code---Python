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

signsList = [rock,paper,scissors]
signsName = ["Rock","Paper","Scissors"]

userInput = int(input("What do you choose?\n"
                  "0 for Rock\n"
                  "1 for Paper\n"
                  "2 for Scissors\n"))

computerInput = random.randint(0,2)

if userInput > 2 or userInput <0:
    print("Value incorrect")
    exit()
else:
    print("You chose:\n" + signsName[userInput] + signsList[userInput])

    print("Computer chose:\n" + signsName[computerInput] + signsList[computerInput])

if userInput == computerInput:
    print("Draw")
elif userInput > computerInput:
  if (userInput or computerInput) == 2:
     if userInput == 2 and computerInput == 0:
        print("You lose")
     elif userInput == 0 and computerInput == 2:
         print("You win")
     else:
         print("You win")
  else:
        print("You win")
else:
    print("You lose")



