
import random
import os

# no magical constants
INITIAL_EMPTY_SQUARE = " "
HUMAN_MARK = "X"
COMPUTER_MARK = "O"
FIRST_MOVE = 'choose'  # options for this constant are "computer",
#                           "player", or "choose"
GAMES_NEEDED_TO_WIN_MATCH = 5


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
def display_board(board):
    os.system('clear')

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
        if 5 in empty_squares(board):    
            square = 5                  
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

def is_computer_first_move():
    while True:
        prompt("Would you like the computer to move first? y/n")
        first_move_choice = input().strip().lower()
        if first_move_choice == "y":
            return True
        elif first_move_choice == "n":
            return None
        prompt("Sorry, that's not a valid choice.")





# Main program loop
def play_tic_tac_toe():
    while True:
        board = new_empty_board()

        player_chose_comp_move_first = None
        while FIRST_MOVE == 'choose':
            player_chose_comp_move_first = is_computer_first_move()
            break

        while FIRST_MOVE == 'computer' or player_chose_comp_move_first:
            computer_choice(board)
            break

        while True:
            display_board(board)

            player_choice(board)
            if someone_won(board) or board_full(board):
                break

            computer_choice(board)
            if someone_won(board) or board_full(board):
                break

        display_board(board)

        if someone_won(board):
            prompt(f"{detect_winner(board)} won!")
        else:
            prompt(f"It's a tie!")
        prompt("Play again? (y or n)")
        answer = input().lower()
        if answer[0] != 'y':
            break
    prompt("Thanks for playing Tic Tac Toe!")

play_tic_tac_toe()