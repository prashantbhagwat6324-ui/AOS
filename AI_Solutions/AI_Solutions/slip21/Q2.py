import itertools

letters = ('G', 'O', 'T', 'U')
digits = range(10)

for perm in itertools.permutations(digits, len(letters)):
    G, O, T, U = perm

    if G == 0 or T == 0:  # No leading zeros
        continue

    GO = G*10 + O
    TO = T*10 + O
    OUT = O*100 + U*10 + T

    if GO + TO == OUT:
        print("Solution Found:")
        print(f"G={G}, O={O}, T={T}, U={U}")
        print(f"{GO} + {TO} = {OUT}")
        break
else:
    print("No solution exists.")
