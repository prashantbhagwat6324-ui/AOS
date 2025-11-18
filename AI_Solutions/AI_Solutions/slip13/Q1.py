# Tic-Tac-Toe using Minimax (exam-ready)

import math
from copy import deepcopy

# Board representation: 3x3 list of lists, '-' for empty
def print_board(b):
    for row in b:
        print(" ".join(row))
    print()

def check_winner(b):
    # Rows, columns, diagonals
    lines = []
    lines.extend(b)  # rows
    lines.extend([[b[r][c] for r in range(3)] for c in range(3)])  # cols
    lines.append([b[i][i] for i in range(3)])  # diag
    lines.append([b[i][2-i] for i in range(3)])  # anti-diag

    for line in lines:
        if line[0] != '-' and line.count(line[0]) == 3:
            return line[0]  # 'X' or 'O'
    # Check draw
    if all(b[r][c] != '-' for r in range(3) for c in range(3)):
        return 'D'  # Draw
    return None  # Game not finished

def get_empty_cells(b):
    return [(r, c) for r in range(3) for c in range(3) if b[r][c] == '-']

# Minimax: returns (score, move)
# Scores: X (maximizer) -> +1, O (minimizer) -> -1, Draw -> 0
def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return 1, None
    if winner == 'O':
        return -1, None
    if winner == 'D':
        return 0, None

    if is_maximizing:
        best_score = -math.inf
        best_move = None
        for (r, c) in get_empty_cells(board):
            board[r][c] = 'X'
            score, _ = minimax(board, False)
            board[r][c] = '-'
            if score > best_score:
                best_score = score
                best_move = (r, c)
        return best_score, best_move
    else:
        best_score = math.inf
        best_move = None
        for (r, c) in get_empty_cells(board):
            board[r][c] = 'O'
            score, _ = minimax(board, True)
            board[r][c] = '-'
            if score < best_score:
                best_score = score
                best_move = (r, c)
        return best_score, best_move

# Helper to get best move for player 'X'
def best_move_for_X(board):
    _, move = minimax(board, True)
    return move

# Example board (partial game); X to move (maximizer)
board = [
    ['X', 'O', 'X'],
    ['-', 'O', '-'],
    ['-', '-', '-']
]

print("Current Board:")
print_board(board)

move = best_move_for_X(board)
print("Best move for X is:", move)
# If you want to apply the move and show result:
if move:
    r, c = move
    board[r][c] = 'X'
    print("Board after X plays:")
    print_board(board)
