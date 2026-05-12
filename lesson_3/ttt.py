
import random
import os

# no magical constants
INITIAL_EMPTY_SQUARE = " "
HUMAN_MARK = "X"
COMPUTER_MARK = "O"

# Make it pretty
def prompt(message):
    print(f"==> {message}")

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
        prompt(f"Choose a square ({", ".join(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break
        prompt("Sorry, that's not a valid choice.")
    board[int(square)] = HUMAN_MARK

def computer_choice(board):
    if len(empty_squares(board)) == 0:
        return
    comp_square = random.choice(empty_squares(board))
    board[comp_square] = COMPUTER_MARK

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], 
        [1, 5, 9], [3, 5, 7], [1, 4, 7],
        [2, 5, 8], [3, 6, 9]
    ]

    for line in winning_lines:
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


# Main program loop
def play_tic_tac_toe():
    while True:
        board = new_empty_board()

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