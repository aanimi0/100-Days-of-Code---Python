import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


rangeOfLetters = range(0,nr_letters)
rangeOfSymbols = range(0,nr_symbols)
rangeOfNumbers = range(0,nr_numbers)


lettersGenerated = []
symbolsGenerated = []
numbersGenerated = []

for let in rangeOfLetters:
    lettersGenerated += random.choice(letters)

for sym in rangeOfSymbols:
    symbolsGenerated += random.choice(symbols)

for num in rangeOfNumbers:
    numbersGenerated += random.choice(numbers)

passwordGenerated = lettersGenerated + symbolsGenerated + numbersGenerated
random.shuffle(passwordGenerated)

# delimiter = ""
# passwordString = delimiter.join(passwordGenerated)

passwordString = ""

for char in passwordGenerated:
    passwordString += char

print(f"Password is: {passwordString}")
