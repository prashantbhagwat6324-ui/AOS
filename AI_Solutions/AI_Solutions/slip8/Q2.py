import random

board = [" " for _ in range(9)]

def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(brd, player):
    win_cond = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # cols
        [0,4,8], [2,4,6]             # diagonals
    ]
    for c in win_cond:
        if brd[c[0]] == brd[c[1]] == brd[c[2]] == player:
            return True
    return False

def is_full(brd):
    return " " not in brd

print("Tic Tac Toe Game!")
print_board()

while True:
    # User Move
    pos = int(input("Enter position (1-9): ")) - 1
    if board[pos] == " ":
        board[pos] = "X"
    else:
        print("Position already taken!")
        continue

    print_board()

    if check_winner(board, "X"):
        print("You win!")
        break

    if is_full(board):
        print("Match Draw!")
        break

    # Computer Move
    print("Computer is playing...")
    empty_positions = [i for i in range(9) if board[i] == " "]
    comp_pos = random.choice(empty_positions)
    board[comp_pos] = "O"

    print_board()

    if check_winner(board, "O"):
        print("Computer wins!")
        break
