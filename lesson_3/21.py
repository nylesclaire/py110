#### Pseudocode to start

# 1. Initialize deck
# 2. Deal cards to player and dealer
# 3. Player turn: hit or stay
#    - repeat until bust or stay
# 4. If player bust, dealer wins.
# 5. Dealer turn: hit or stay
#    - repeat until total >= 17
# 6. If dealer busts, player wins.
# 7. Compare cards and declare winner.

import copy
import random

FULL_DECK = [
    ["A", "H"], ["2", "H"], ["3", "H"], ["4", "H"],
    ["5", "H"], ["6", "H"], ["7", "H"], ["8", "H"], ["9", "H"],
    ["10", "H"], ["J", "H"], ["Q", "H"], ["K", "H"], 
    ["A", "D"], ["2", "D"], ["3", "D"], ["4", "D"],
    ["5", "D"], ["6", "D"], ["7", "D"], ["8", "D"], ["9", "D"],
    ["10", "D"], ["J", "D"], ["Q", "D"], ["K", "D"], 
    ["A", "C"], ["2", "C"], ["3", "C"], ["4", "C"],
    ["5", "C"], ["6", "C"], ["7", "C"], ["8", "C"], ["9", "C"],
    ["10", "C"], ["J", "C"], ["Q", "C"], ["K", "C"],
    ["A", "S"], ["2", "S"], ["3", "S"], ["4", "S"],
    ["5", "S"], ["6", "S"], ["7", "S"], ["8", "S"], ["9", "S"],
    ["10", "S"], ["J", "S"], ["Q", "S"], ["K", "S"],  
]

CARD_VALUES = {"2": 2,
               "3": 3,
               "4": 4,
               "5": 5,
               "6": 6,
               "7": 7,
               "8": 8, 
               "9": 9, 
               "10": 10, 
               "J": 10, 
               "Q": 10,
               "K": 10, 
               "A": "A"}

def prompt(message):
    print(f"==> {message}")

def shuffle(deck):
    random.shuffle(deck)

def deal_initial_two_cards(deck):
    return [deck.pop(), deck.pop()]

def deal_one_card(deck): 
    return deck.pop()

def determine_hand_total(hand):
    hand_values = [CARD_VALUES[card[0]] for card in hand]
    sum_values = 0
    for value in hand_values:
        if value == "A":
            sum_values += 11
        else:
            sum_values += value

    number_of_aces = hand_values.count("A")
    while sum_values > 21 and number_of_aces:
        sum_values -= 10
        number_of_aces -= 1

    return sum_values

def busted(hand):
    if determine_hand_total(hand) > 21:
        return True


def play_again():
    prompt("Want to play again? (y or n)")
    answer = input().lower()
    if answer[0] == 'y':
        return True


def display_the_table(player_hand, dealer_hand):
    prompt("The dealer's cards:")
    suits = [f"|{f"{card[1]}"}        |" for card in dealer_hand]
    card_faces = [f"|{f"{card[0]}".center(9)}|" for card in dealer_hand]
    card_top_bot_line = [f"|---------|" for card in dealer_hand]
    print(*card_top_bot_line, sep='   ')
    print(*suits, sep='   ')
    print(*card_faces, sep='   ')
    print(*card_top_bot_line, sep='   ')
    print(f"")
    print(f"")

    prompt("Your cards:")
    suits = [f"|{f"{card[1]}"}        |" for card in player_hand]
    card_faces = [f"|{f"{card[0]}".center(9)}|" for card in player_hand]
    card_top_bot_line = [f"|---------|" for card in player_hand]
    print(*card_top_bot_line, sep='   ')
    print(*suits, sep='   ')
    print(*card_faces, sep='   ')
    print(*card_top_bot_line, sep='   ')
    prompt(f"Your hand total: {determine_hand_total(player_hand)}")
    print(f"")


### working on Player turn

def player_turn(player_hand, dealer_hand, deck):   # will return new player_hand list
    while True:
        display_the_table(player_hand, dealer_hand)
        prompt("Hit or stay? (h or s)")
        answer = input().lower()

        if answer[0] == "s":
            return player_hand
        
        player_hand.append(deal_one_card(deck))

        if busted(player_hand):
            return player_hand






# Main game loop begins here
def from_welcome_to_finish():
    prompt("Welcome to Twenty-One.")
    # maybe display rules?
    dealer_wins = 0
    player_wins = 0

    while True:
        winner = play_21()

        if winner == "dealer":
            dealer_wins += 1
        elif winner == "player":
            player_wins += 1

        if not play_again():
            break
    prompt("Thanks for playing Twenty-One!")



def play_21():
    deck = copy.deepcopy(FULL_DECK)

    shuffle(deck)
    player_hand = deal_initial_two_cards(deck) 
    dealer_hand = deal_initial_two_cards(deck) 

    player_hand = player_turn(player_hand, dealer_hand, deck)
    if busted(player_hand):
        display_the_table(player_hand, dealer_hand)
        prompt(f"AW DANG! You BUSTED!") # consider making this bubble letters!
        print(f"")
        return "dealer"
    else:
        prompt("You chose to stay. Now for the dealer's turn.")

#     dealer_turn()
# #    if busted():
# #        display message
# #        return winner

#     compare_hands() # this should return the winner or "tie"





from_welcome_to_finish()