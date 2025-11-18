def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Left diagonal
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Right diagonal
    i, j = row-1, col+1
    while i >= 0 and j < n:
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(n):
    board = [-1] * n
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions


n = int(input("Enter n: "))
solutions = solve_n_queens(n)

print("Number of solutions:", len(solutions))
print("One solution:")

sol = solutions[0]
for r in range(n):
    row = ["Q" if sol[r] == c else "." for c in range(n)]
    print(" ".join(row))
