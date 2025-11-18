# 8-Queens Problem - backtracking solver (exam-ready)

def is_safe(board, row, col, n=8):
    # Check column above
    for i in range(row):
        if board[i] == col:
            return False
    # Check upper-left diagonal
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1; j -= 1
    # Check upper-right diagonal
    i, j = row-1, col+1
    while i >= 0 and j < n:
        if board[i] == j:
            return False
        i -= 1; j += 1
    return True

def solve_n_queens(n=8):
    solutions = []
    board = [-1] * n  # board[row] = col where queen is placed

    def backtrack(row):
        if row == n:
            # convert to visual board and store
            sol = []
            for r in range(n):
                row_str = ['.'] * n
                row_str[board[r]] = 'Q'
                sol.append(" ".join(row_str))
            solutions.append(sol)
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions

# Run and print one solution (or all if you want)
solutions = solve_n_queens(8)
print("Number of solutions found:", len(solutions))
print("\nOne valid 8-Queens solution:")
for line in solutions[0]:
    print(line)
