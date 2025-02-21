from idlelib.debugger_r import start_remote_debugger
from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculator_dictionary ={"+": add,
                        "-": subtract,
                        "*": multiply,
                        "/": divide,
                        }

def calculator():
    print(logo)

    first_number = float(input("Please type the first number\n"))

    should_continue = True

    while should_continue:
        for symbol in calculator_dictionary:
            print(symbol)

        user_operation = input("Please choose the operation")

        second_number = float(input("Please type your next number?"))

        result = calculator_dictionary[user_operation](first_number,second_number)

        print(f"{first_number} {user_operation} {second_number} = {result} ")

        choice = input(f"Do you want to continue calculating with {result} Y or N?: \n").upper()
        if choice == "Y":
            first_number = result
        else:
            process_start = False
            print("\n" * 20)
            calculator()

calculator()