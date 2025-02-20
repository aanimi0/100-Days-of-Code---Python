#print("\n" * 100) #to clear the screen
from art import logo
print(logo)
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"Winner is {winner} with the bid {highest_bid}")


game_ongoing = True
bids = {}

while game_ongoing:

    user_name = input("Please type your name\n")
    user_bid = int(input("Please type the amount: $"))
    bids[user_name] = user_bid
    check_continue = input("Do you want to continue yes or no?\n")
    if check_continue == 'no':
        game_ongoing = False
        find_highest_bidder(bids)
    else:
        print("\n" * 20)


