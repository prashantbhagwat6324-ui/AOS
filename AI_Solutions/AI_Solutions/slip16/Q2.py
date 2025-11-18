import random

board = [' ' for _ in range(9)]

def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(brd, mark):
    win_pos = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(brd[a] == brd[b] == brd[c] == mark for a,b,c in win_pos)

def get_empty_positions(brd):
    return [i for i,v in enumerate(brd) if v == ' ']

def player_move():
    pos = int(input("Enter position (1-9): ")) - 1
    if board[pos] == ' ':
        board[pos] = 'X'

def computer_move():
    pos = random.choice(get_empty_positions(board))
    board[pos] = 'O'
    print(f"Computer placed O at position {pos+1}")

def play_game():
    print("Tic Tac Toe Game")
    print_board()

    for _ in range(9):
        player_move()
        print_board()
        if check_winner(board, 'X'):
            print("Player Wins!")
            return

        if not get_empty_positions(board):
            break

        computer_move()
        print_board()
        if check_winner(board, 'O'):
            print("Computer Wins!")
            return

    print("Game Draw!")

play_game()
