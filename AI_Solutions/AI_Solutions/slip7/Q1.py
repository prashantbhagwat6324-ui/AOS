import math

# Display Board
def print_board(board):
    for row in board:
        print(row)
    print()

# Check Winner
def check_winner(board):
    wins = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    for w in wins:
        if w.count(w[0]) == 3 and w[0] != '-':
            return w[0]
    return None

# Check Empty Cells
def get_empty_cells(board):
    empty = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                empty.append((i, j))
    return empty

# Minimax with Alpha-Beta
def alphabeta(board, depth, alpha, beta, is_max):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif not get_empty_cells(board):
        return 0

    if is_max:  # Maximizing for X
        best = -math.inf
        for (i, j) in get_empty_cells(board):
            board[i][j] = 'X'
            val = alphabeta(board, depth + 1, alpha, beta, False)
            board[i][j] = '-'
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best

    else:  # Minimizing for O
        best = math.inf
        for (i, j) in get_empty_cells(board):
            board[i][j] = 'O'
            val = alphabeta(board, depth + 1, alpha, beta, True)
            board[i][j] = '-'
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

# Best Move for X
def best_move(board):
    best_val = -math.inf
    move = (-1, -1)

    for (i, j) in get_empty_cells(board):
        board[i][j] = 'X'
        val = alphabeta(board, 0, -math.inf, math.inf, False)
        board[i][j] = '-'

        if val > best_val:
            best_val = val
            move = (i, j)
    return move


# Main Code
board = [
    ['X', 'O', '-'],
    ['-', 'O', '-'],
    ['X', '-', '-']
]

print("Current Board:")
print_board(board)

move = best_move(board)
print("Best Move for X:", move)
