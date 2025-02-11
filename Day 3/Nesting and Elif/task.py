print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")

    age = int(input("What is your age?"))
    if age <= 12:
        bill = 5
        print(f"Ticket is ${bill}")
    elif age <= 18:
        bill = 12
        print(f"Ticket is ${bill}")
    else:
        bill = 20
        print(f"Ticket is ${bill}")

    wants_photo = input("Do you want a photo? y or n")

    if wants_photo == "y":
        bill += 3

    print(f"Ticket is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
