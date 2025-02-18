# def greet():
#     print("Hello")
#     print("I am Mr Robot")
#     print("How may I assist you today?")
#
# greet()

#function with input
def greetWithName(name):
    print(f"Hello {name}")
    print("I am Mr Robot")
    print(f"How may I assist you today {name}?")

greetWithName("FFF")

def life_in_weeks(number):
    time_to_live = 90  # in years
    user_input = number

    remaining_years = time_to_live - user_input
    remaining_months = remaining_years * 52

    print(f"You have {remaining_months} weeks left.")


life_in_weeks(89)