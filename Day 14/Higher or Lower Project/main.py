from art import logo
from art import vs
from game_data import data
import random

def generate_details():
    choice = random.choice(data)
    return choice

def calculate_answer(a_list,b_list):
    a_follower_count = 0
    b_follower_count = 0

    for key in a_list:
        if key == "follower_count":
            a_follower_count = a_list[key]

    for key in b_list:
        if key == "follower_count":
            b_follower_count = b_list[key]

    if a_follower_count > b_follower_count:
        return 'A'
    else:
        return 'B'


a_dict = generate_details()
b_dict = generate_details()

score = 0
game_on = True

while game_on:
    print(logo)

    a_name = a_dict["name"]
    a_description = a_dict["description"]
    a_country = a_dict["country"]

    b_name = b_dict["name"]
    b_description = b_dict["description"]
    b_country = b_dict["country"]

    print(calculate_answer(a_dict,b_dict))
    correct_answer = calculate_answer(a_dict,b_dict)

    print(f"Compare A: {a_name}, {a_description}, from {a_country}")

    print(vs)

    print(f"Compare B: {b_name}, {b_description}, from {b_country}")

    user_input = input("Who has more followers? Type 'A' or 'B':").upper()

    if user_input == correct_answer:
        a_dict = b_dict
        b_dict = generate_details()
        score += 1
        print(f"You are right! Current score: {score}")
        print("\n" * 20)
    else:
        game_on = False
        print(f"Sorry, that's wrong. Final score: {score}")