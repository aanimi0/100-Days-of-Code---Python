import random
from art import logo

#cards_faces = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")

def compare(user,computer):
    if user == computer:
        print("Draw!")
        print(f"Your score: {user_score}")
        print(f"Computer score: {computer_score}")
    elif computer == 21:
        print("You lost!")
        print(f"Your score: {user_score}")
        print(f"Computer score: {computer_score}")
    elif user == 21:
        print("You win!")
        print(f"Your score: {user_score}")
        print(f"Computer score: {computer_score}")
    elif user > 21:
        print("You lost! Bust")
        print(f"Your score: {user_score}")
        print(f"Computer score: {computer_score}")
    elif computer > 21:
        print("You win! computer went bust!")
        print(f"Your score: {user_score}")
        print(f"Computer score: {computer_score}")
    elif computer > user < 21:
        print("You lost! Computer has a higher score")
        print(f"Your score: {user_score}")
        print(f"Computer score: {computer_score}")
    elif user > computer < 21:
        print("You win! With a higher score")
        print(f"Your score: {user_score}")
        print(f"Computer score: {computer_score}")

def calculate_score(card_list):
    total_score = 0
    cards_in_hand = len(card_list)
    for card in card_list:
        total_score += card
        if card == 11:
            if total_score > 21:
                card_list.remove(11)
                card_list.append(1)
                total_score -= 10
    if cards_in_hand == 2 and total_score == 21:
        return 0
    return total_score

def deal_cards(in_hand):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    if not in_hand:
        in_hand.append(random.choice(cards))
        in_hand.append(random.choice(cards))
    else:
        in_hand.append(random.choice(cards))

game_on = True
while game_on:
    print(logo)
    #user_plays = input("Would you like to start blackjack? 'y' or 'n'\n")
    #if not user_plays == 'y':
    #    game_on = False


    user_hand = []
    computer_hand = []

    deal_cards(user_hand)
    deal_cards(computer_hand)

    calculate_score(user_hand)
    calculate_score(computer_hand)

    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)

    print(f"Your hand is: {user_hand}. Score: {user_score}")
    print(f"Computer's first hand is: {computer_hand[0]}.")


    user_turn = True
    while user_turn:
        if user_hand == 0:
            print('Blackjack! You win!')
            user_turn = False
        elif computer_score == 0:
            user_turn = False
            print('You Lose! Blackjack')

        new_card = input("Draw another card? 'y' or 'n'?\n")
        if new_card == 'y':
            deal_cards(user_hand)
            calculate_score(user_hand)
            user_score = calculate_score(user_hand)
            if  user_score > 21:
                print(f"Bust! You lost. Score: {user_score}")
                user_turn = False
            else:
                print(f"Your hand is: {user_hand}. Score: {user_score}")

        else:
            user_turn = False

    while computer_score < 17 and computer_score != 0:
        deal_cards(computer_hand)
        computer_score = calculate_score(computer_hand)
        print(f"Computer's hand is: {computer_hand}.Score{computer_score}")

    compare(user_score,computer_score)
    user_restart = input("Do you want to restart the game 'y' or 'n'?\n")
    if user_restart == 'y':
        game_on = True
        print("\n" * 20)
    else:
        game_on = False
        print("Goodbye!")
