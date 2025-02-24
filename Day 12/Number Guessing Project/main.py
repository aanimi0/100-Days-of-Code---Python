from art import logo
from random import randint

print(logo)
HARD_LEVEL_ATTEMPTS = 10
EASY_LEVEL_ATTEMPTS = 5

def set_difficulty():
    if difficulty == 'easy':
        return HARD_LEVEL_ATTEMPTS
    elif difficulty == 'hard':
        return EASY_LEVEL_ATTEMPTS
    else:
        print("Not a valid difficulty. Goodbye!")
        return 0


def check_answer(user_guess,computer_guess,turns):
    """checks answers against guess and returns the number of turns remaining"""
    if computer_guess > user_guess:
        print("Too low.")
        print("Guess again.")
        return turns - 1
    if computer_guess < user_guess:
        print("Too high.")
        print("Guess again.")
        return turns - 1


def game():
    attempts = set_difficulty()

    guess = 0


    while guess != computer_number:
        print(f"You have {attempts} attempts remaining to guess the number")

        guess = int(input("Make a guess:\n"))

        attempts = check_answer(user_guess = guess, computer_guess = computer_number, turns = attempts)

        if guess == computer_number:
            print("You guessed the number! CONGRATS!")
            return
        if attempts == 0:
            print("You ran out of guesses! You lost!")
            return

computer_number = randint(1,100)
print(f"number selected {computer_number}")

print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard'\n")

game()



