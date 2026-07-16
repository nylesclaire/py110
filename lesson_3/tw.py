#### Twenty-One

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

BIG_TOTAL = 21
DEALER_HITS_UNTIL = 17

# This constant can be turned 'off' or 'on' based on whether you'd like to
# play individual games, or a 'best of' contest
MATCH_MODE = True
GAMES_NEEDED_TO_WIN_MATCH = 3


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
    while sum_values > BIG_TOTAL and number_of_aces:
        sum_values -= 10
        number_of_aces -= 1

    return sum_values

def busted(hand_tot):
    return hand_tot > BIG_TOTAL

def play_again():
    prompt("Want to play again? (y or n)")
    while True:
        answer = input()
        if answer == "" or answer.lower()[0] not in ['y', 'n']:
            prompt("Try a valid answer! (y or n)")
            continue
        if answer.lower()[0] == 'y':
            return True
        return False

def play_again_match():
    prompt("Want to play another match? (y or n)")
    while True:
        answer = input()
        if answer == "" or answer.lower()[0] not in ['y', 'n']:
            prompt("Try a valid answer! (y or n)")
            continue
        if answer.lower()[0] == 'y':
            return True
        return False


def display_the_table(player_hand, dealer_hand, player_tot, dealer_tot,
                      mystery=True):
    prompt("The dealer's cards:")

    if mystery:
        dealer_hand_display = [["???", " "]] * (len(dealer_hand) - 1)
        dealer_hand_display.insert(0, dealer_hand[0])
    else:
        dealer_hand_display = dealer_hand

    d_suits = [f"|{f"{card[0]}".ljust(9)}|" for card in dealer_hand_display]
    d_card_faces = [f"|{f"{card[1]}".center(9)}|"
                    for card in dealer_hand_display]
    d_card_top_bot_line = ["|---------|" for card in dealer_hand_display]

    print(*d_card_top_bot_line, sep='   ')
    print(*d_suits, sep='   ')
    print(*d_card_faces, sep='   ')
    print(*d_card_top_bot_line, sep='   ')
    print("")
    print("")

    prompt("Your cards:")
    p_suits = [f"|{f"{card[0]}".ljust(9)}|" for card in player_hand]
    p_card_faces = [f"|{f"{card[1]}".center(9)}|" for card in player_hand]
    p_card_top_bot_line = ["|---------|" for card in player_hand]

    print(*p_card_top_bot_line, sep='   ')
    print(*p_suits, sep='   ')
    print(*p_card_faces, sep='   ')
    print(*p_card_top_bot_line, sep='   ')
    if not mystery:
        prompt(f"The dealer's hand total: {dealer_tot}")
    prompt(f"Your hand total: {player_tot}")
    print("")


#returns new player_hand list, player_tot
def player_turn(player_hand, dealer_hand, player_tot, dealer_tot, deck):
    prompt("After shuffling and dealing...")
    print("")

    while True:
        display_the_table(player_hand, dealer_hand, player_tot, dealer_tot)

        prompt("Hit or stay? (h or s)")
        while True:
            answer = input().lower()
            if answer[0] == "s":
                os.system('clear')
                prompt("You chose to stay. Now for the dealer's turn.")
                print("")
                return player_hand, player_tot
            if answer[0] == "h":
                break
            prompt("That's an invalid answer, try again.")

        player_hand.append(deal_one_card(deck))
        player_tot = determine_hand_total(player_hand)
        os.system('clear')
        prompt("You chose to hit....")
        print("")

        if busted(player_tot):
            display_the_table(player_hand, dealer_hand, player_tot, dealer_tot)
            prompt("AW DANG! You BUSTED!") # consider making this bubble letters!
            print("")
            return player_hand, player_tot


# will return new dealer_hand list, dealer_tot
def dealer_turn(player_hand, dealer_hand, player_tot, dealer_tot, deck):
    dealer_hits = 0
    while True:
        if busted(dealer_tot):
            display_the_table(player_hand, dealer_hand, player_tot, dealer_tot,
                          mystery=False)
            if dealer_hits == 1:
                prompt(f"Heck yeah! The dealer hit 1 time, "
                   "and then busted!")
            else:
                prompt(f"Heck yeah! The dealer hit {dealer_hits} times, "
                   "and then busted!")
            print("")
            return dealer_hand, dealer_tot

        if dealer_tot >= DEALER_HITS_UNTIL:
            display_the_table(player_hand, dealer_hand, player_tot, dealer_tot)
            if dealer_hits == 0:
                prompt(f"The dealer stayed...")
            elif dealer_hits == 1:
                prompt(f"The dealer hit 1 time, and then stayed...")
            else:
                prompt(f"The dealer hit {dealer_hits} times, and then stayed...")
            input("==> Let's see how those hands measure up. Press Enter.")
            os.system('clear')
            return dealer_hand, dealer_tot

        dealer_hand.append(deal_one_card(deck))
        dealer_hits += 1
        dealer_tot = determine_hand_total(dealer_hand)


# will return the winner
def compare_hands(player_tot, dealer_tot):
    if player_tot > dealer_tot:
        prompt("YOU WON! Niiiice.")
        print("")
        return "player"
    if dealer_tot > player_tot:
        prompt("The dealer won. Bummer.")
        print("")
        return "dealer"
    prompt("It's a tie! Wild.")
    print("")
    return None

rules_string = f'''
    * * * The Rules * * *
    -Your goal: get as close to {BIG_TOTAL} as possible without going over (a bust!).
    -2's through 10's are worth their value; Jacks, Queens, and Kings: 10.
    -Aces are worth 1 or 11, depending on what else is in your hand.

    -You & the dealer will start with 2 cards each-- you'll be able to see
    only one of the dealer's cards.
    -'Hit' (get another card) as many times as you like, until you either
    bust or choose to 'stay'.
    -On the dealer's turn, they will hit until their total is at least {DEALER_HITS_UNTIL},
    or until they bust.
    -If both players have stayed, the totals of their hands are compared
    to see whose is closest to {BIG_TOTAL}!
'''


###############
# Program loop begins here
def from_welcome_to_finish():
    os.system('clear')
    prompt("Welcome to Twenty-One.")
    print("")
    print(rules_string)
    print("--------------------------------------")
    if MATCH_MODE:
        prompt(f"Let's see who can win {GAMES_NEEDED_TO_WIN_MATCH} games first!")
    input("==> Ready to start? Press Enter.")

    while True:
        dealer_wins = 0
        player_wins = 0

        while True:
            os.system('clear')
            winner = play_21()

            if winner == "dealer":
                dealer_wins += 1
            elif winner == "player":
                player_wins += 1

            print("--------------------------------------")
            if MATCH_MODE:
                someone_won = False
                prompt(f"Dealer: {dealer_wins} | Player: {player_wins}")
                if dealer_wins == GAMES_NEEDED_TO_WIN_MATCH:
                    prompt("Dang. The dealer won the match.")
                    someone_won = True
                    break
                if player_wins == GAMES_NEEDED_TO_WIN_MATCH:
                    prompt("WOOHOO! You won the match! ")
                    someone_won = True
                    break

            if not play_again():
                break

        if MATCH_MODE and someone_won:
            if play_again_match():
                continue
        break

    prompt("Thanks for playing Twenty-One!")


# Game loop itself begins here
def play_21():
    deck = copy.deepcopy(FULL_DECK)

    shuffle(deck)
    player_hand = deal_initial_two_cards(deck)
    dealer_hand = deal_initial_two_cards(deck)

    player_tot = determine_hand_total(player_hand)
    dealer_tot = determine_hand_total(dealer_hand)

    ## Player's turn
    player_hand, player_tot = player_turn(player_hand, dealer_hand, player_tot,
                              dealer_tot, deck)
    if busted(player_tot):
        return "dealer"

    ## Dealer's turn
    dealer_hand, dealer_tot = dealer_turn(player_hand, dealer_hand, player_tot,
                              dealer_tot, deck)
    if busted(dealer_tot):
        return "player"

    ## If both players stayed:
    prompt("Here's the reveal!")
    print("")
    display_the_table(player_hand, dealer_hand, player_tot, dealer_tot,
                      mystery=False)

    return compare_hands(player_tot, dealer_tot)





from_welcome_to_finish()