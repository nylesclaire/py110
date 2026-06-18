
import random
import os

# no magical quantities
INITIAL_EMPTY_SQUARE = " "
HUMAN_MARK = "X"
COMPUTER_MARK = "O"
MIDDLE_SQUARE = 5
FIRST_MOVE = 'choose'  # options for this constant are "computer",
#                           "player", or "choose"
GAMES_NEEDED_TO_WIN_MATCH = 3

WINNING_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], 
        [1, 5, 9], [3, 5, 7], [1, 4, 7],
        [2, 5, 8], [3, 6, 9]
    ]

# Make it pretty
def prompt(message):
    print(f"==> {message}")

def join_or(lst, delim=', ', end_word='or'):
    match len(lst):
        case 0:
            return ""
        case 1:
            return str(lst[0])
        case 2:
            return f"{str(lst[0])} {end_word} {str(lst[1])}"
    
    leading_lst = [str(item) + delim for item in lst[0:-1]]
    return f"{"".join(leading_lst)}{end_word} {str(lst[-1])}"
    

# Display the board
def display_board(board, player_score, computer_score,
                  current_game_number):
    os.system('clear')

    prompt(f'''Game Number {current_game_number}
    Remember, {GAMES_NEEDED_TO_WIN_MATCH} wins are needed to win the match.''')
    print(f"")
    prompt(f"You: {player_score} | Computer: {computer_score}")
    print(f"")
    prompt(f"You are {HUMAN_MARK}. Computer is {COMPUTER_MARK}.")
    print(f"")
    print(f"----------|---------|----------")
    print(f"|         |         |         |")
    print(f"|    {board[1]}    |    {board[2]}    |    {board[3]}    |")
    print(f"|         |         |         |")
    print(f"----------|---------|----------")
    print(f"|         |         |         |")
    print(f"|    {board[4]}    |    {board[5]}    |    {board[6]}    |")
    print(f"|         |         |         |")
    print(f"----------|---------|----------")
    print(f"|         |         |         |")
    print(f"|    {board[7]}    |    {board[8]}    |    {board[9]}    |")
    print(f"|         |         |         |")
    print(f"----------|---------|----------")
    print(f"")

def new_empty_board():
    return {square: INITIAL_EMPTY_SQUARE for square in range(1, 10)}

def empty_squares(board):
    return [key for key, value in board.items() 
                     if value == INITIAL_EMPTY_SQUARE]

def player_choice(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break
        prompt("Sorry, that's not a valid choice.")
    board[int(square)] = HUMAN_MARK

def computer_choice(board):
    square = detect_at_risk_square(board, COMPUTER_MARK)
    if not square:
        square = detect_at_risk_square(board, HUMAN_MARK)
    if not square:                      
        if MIDDLE_SQUARE in empty_squares(board):    
            square = MIDDLE_SQUARE               
    if not square:
        square = random.choice(empty_squares(board)) 
    board[square] = COMPUTER_MARK

def detect_at_risk_square(board, marker_of_the_threat):
    for line in WINNING_LINES:
        marks = [board[item] for item in line]
        if (marks.count(marker_of_the_threat) == 2
                and marks.count(INITIAL_EMPTY_SQUARE) == 1):
            return line[marks.index(INITIAL_EMPTY_SQUARE)]


def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARK
                and board[sq2] == HUMAN_MARK
                and board[sq3] == HUMAN_MARK):
            return 'Player'
        elif(board[sq1] == COMPUTER_MARK
                and board[sq2] == COMPUTER_MARK
                and board[sq3] == COMPUTER_MARK):
            return 'Computer'
    return None

def choosing_first_move():
    while True: 
        prompt('''In each game of the match, the player who gets to
    move first will alternate. Select who will move first in
    the first game. Enter c (computer) or m (me).''')
        first_move_choice = input().strip().lower()
        if first_move_choice == "c":
            return 'computer'
        elif first_move_choice == "m":
            return 'player'
        prompt("Sorry, that's not a valid choice. Enter c or m.")

def play_again():
    prompt("Play again? (y or n)")
    answer = input().lower()
    while answer not in ["y", "yes", "yup", "n", "no", "nope"]:
        prompt("Please enter y or n")
        answer = input().lower().strip()
    return answer in ["y", "yes", "yup"]

def choose_square(board, current_player):
    if current_player == 'player':
        player_choice(board)
    else: 
        computer_choice(board)

def alternate_player(current_player):
    if current_player == 'player':
        return 'computer'
    return 'player'




# Main program loops
def play_tic_tac_toe(player_score, computer_score,
                     current_game_number, first_to_move):

    board = new_empty_board()

    current_player = first_to_move

    display_board(board, player_score, computer_score, 
                          current_game_number)

    while True:
            
        choose_square(board, current_player)

        current_player = alternate_player(current_player)

        display_board(board, player_score, computer_score, 
                current_game_number)
        
        if someone_won(board) or board_full(board):
            break
            
    if someone_won(board):
        prompt(f"{detect_winner(board)} won!")
    else:
        prompt(f"It's a tie!")

    return detect_winner(board)


def play_match():
    current_game_number = 1
    player_score = 0
    computer_score = 0

    first_to_move = FIRST_MOVE
    if first_to_move == "choose":
        first_to_move = choosing_first_move()

    while True:
        
        winner = play_tic_tac_toe(player_score, computer_score, 
                                    current_game_number, 
                                    first_to_move)

        current_game_number += 1

        first_to_move = alternate_player(first_to_move)

        match winner:
            case 'Player':
                player_score += 1
            case 'Computer':
                computer_score += 1
            
        if player_score == GAMES_NEEDED_TO_WIN_MATCH:
            prompt(f"-------------------------------------")
            prompt(r'''You are the 
                           _            _                       _ 
                          | |          (_)                     | |
  __ _ _ __ __ _ _ __   __| | __      ___ _ __  _ __   ___ _ __| |
 / _` | '__/ _` | '_ \ / _` | \ \ /\ / / | '_ \| '_ \ / _ \ '__| |
| (_| | | | (_| | | | | (_| |  \ V  V /| | | | | | | |  __/ |  |_|
 \__, |_|  \__,_|_| |_|\__,_|   \_/\_/ |_|_| |_|_| |_|\___|_|  (_)
  __/ |                                                           
 |___/                                                             
                   ''')
            break
        elif computer_score == GAMES_NEEDED_TO_WIN_MATCH:
            prompt(f"-------------------------------------")
            prompt(r'''
 _   _                                            _                                       __
| | | |                                          | |                                   _ / /
| |_| |__   ___    ___ ___  _ __ ___  _ __  _   _| |_ ___ _ __  __      _____  _ __   (_) | 
| __| '_ \ / _ \  / __/ _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__| \ \ /\ / / _ \| '_ \    | | 
| |_| | | |  __/ | (_| (_) | | | | | | |_) | |_| | ||  __/ |     \ V  V / (_) | | | |  _| | 
 \__|_| |_|\___|  \___\___/|_| |_| |_| .__/ \__,_|\__\___|_|      \_/\_/ \___/|_| |_| (_) | 
                                     | |                                                 \_\
                                     |_|                                                    
                   ''')
            break   

        if not play_again():
            return "DONE"


def from_welcome_to_finish():
    print(r'''
 _____ _        _____            _____          
|_   _(_)      |_   _|          |_   _|         
  | |  _  ___    | | __ _  ___    | | ___   ___ 
  | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ \
  | | | | (__    | | (_| | (__    | | (_) |  __/
  \_/ |_|\___|   \_/\__,_|\___|   \_/\___/ \___|
                                                
                                                ''')

    prompt(f'''Let's play Tic Tac Toe!\n
    First to win {GAMES_NEEDED_TO_WIN_MATCH} games wins the match.
    -------------------------------------'''
    )
    while True:
        if play_match() == "DONE":
            break
        else: 
            prompt("What an incredible match!")
            if not play_again():
                break

    prompt("Thanks for playing Tic Tac Toe!")

from_welcome_to_finish()