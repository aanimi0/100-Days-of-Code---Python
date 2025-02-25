age = 0
try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed an invalid number.")

if age > 18:
    print(f"You can drive at age {age}.")
