def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row-1, col+1
    while i >= 0 and j < 4:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_queens(board, row):
    if row == 4:
        return True

    for col in range(4):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve_queens(board, row + 1):
                return True

            board[row][col] = 0  # backtrack

    return False


# Main program
board = [[0] * 4 for _ in range(4)]

if solve_queens(board, 0):
    print("Solution for 4-Queens:")
    for r in board:
        print(r)
else:
    print("No solution found.")
