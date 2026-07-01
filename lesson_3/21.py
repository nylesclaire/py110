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
import os

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


def display_the_table(player_hand, dealer_hand, mystery=True):
    prompt("The dealer's cards:")

    if mystery:
        dealer_hand_display = [["???", " "]] * (len(dealer_hand) - 1)
        dealer_hand_display.insert(0, dealer_hand[0])
    else:
        dealer_hand_display = dealer_hand

    d_suits = [f"|{f"{card[0]}".ljust(9)}|" for card in dealer_hand_display]
    d_card_faces = [f"|{f"{card[1]}".center(9)}|" for card in dealer_hand_display]
    d_card_top_bot_line = [f"|---------|" for card in dealer_hand_display]

    print(*d_card_top_bot_line, sep='   ')
    print(*d_suits, sep='   ')
    print(*d_card_faces, sep='   ')
    print(*d_card_top_bot_line, sep='   ')
    print(f"")
    print(f"")

    prompt("Your cards:")
    p_suits = [f"|{f"{card[0]}".ljust(9)}|" for card in player_hand]
    p_card_faces = [f"|{f"{card[1]}".center(9)}|" for card in player_hand]
    p_card_top_bot_line = [f"|---------|" for card in player_hand]

    print(*p_card_top_bot_line, sep='   ')
    print(*p_suits, sep='   ')
    print(*p_card_faces, sep='   ')
    print(*p_card_top_bot_line, sep='   ')
    if not mystery:
        prompt(f"The dealer's hand total: {determine_hand_total(dealer_hand)}")
    prompt(f"Your hand total: {determine_hand_total(player_hand)}")
    print(f"")


def player_turn(player_hand, dealer_hand, deck):   # will return new player_hand list
    prompt("After shuffling and dealing...")
    print(f"")
    
    while True:
        display_the_table(player_hand, dealer_hand)
        prompt("Hit or stay? (h or s)")
        answer = input().lower()

        if answer[0] == "s":
            return player_hand
        
        player_hand.append(deal_one_card(deck))
        os.system('clear')
        prompt("You chose to hit....")
        print(f"")

        if busted(player_hand):
            return player_hand

def dealer_turn(dealer_hand, deck): # will return new dealer_hand list
    while True:
        if busted(dealer_hand):
            return dealer_hand
        elif determine_hand_total(dealer_hand) >= 17:
            return dealer_hand
        
        dealer_hand.append(deal_one_card(deck))

def compare_hands(player_hand, dealer_hand): # will return the winner
    player_tot = determine_hand_total(player_hand)
    dealer_tot = determine_hand_total(dealer_hand)

    # prompt(f"Your hand total: {player_tot}")
    # prompt(f"The dealer's hand total: {dealer_tot}")
    # print(f"")

    if player_tot > dealer_tot:
        prompt("YOU WON! Niiiice.")
        print(f"")
        return "player"
    elif dealer_tot > player_tot:
        prompt("The dealer won. Bummer.")
        print(f"")
        return "dealer"
    else:
        prompt("It's a tie! Wild.")
        print(f"")
        return None

    

# Main game loop begins here
def from_welcome_to_finish():
    prompt("Welcome to Twenty-One.")
    print(f"")
    print("Here's where the rules will go when Nyles finishes this.") # finish!
    print("--------------------------------------")
    input(f"==> Ready to start? Press Enter.")
    
    dealer_wins = 0
    player_wins = 0

    while True:
        os.system('clear')
        winner = play_21()

        if winner == "dealer":
            dealer_wins += 1
        elif winner == "player":
            player_wins += 1

# Want to possibly implement here, a way to show the player a tallying
# of games won and/or a "best of 5" type thing.

        print("--------------------------------------")
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
        os.system('clear')
        prompt("You chose to stay. Now for the dealer's turn.")
        print(f"")

    dealer_hand = dealer_turn(dealer_hand, deck)
    if busted(dealer_hand):
        display_the_table(player_hand, dealer_hand, mystery=False)
#       figure out how to display here, something like:
#       "The dealer hit twice and then busted!"

        prompt(f"Heck yeah! The dealer busted!")
        print(f"")
        return "player"
    else:
        display_the_table(player_hand, dealer_hand)
        #       figure out how to display here, something like:
#       "The dealer hit three times and then stayed."
        prompt("The dealer stayed...")
        input(f"==> Let's see how those hands measure up. Press Enter.")
        os.system('clear')

    prompt("Here's the reveal!")
    print(f"")
    display_the_table(player_hand, dealer_hand, mystery=False)
    return compare_hands(player_hand, dealer_hand)





from_welcome_to_finish()