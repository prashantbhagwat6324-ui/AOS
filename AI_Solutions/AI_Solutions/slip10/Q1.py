import itertools

letters = ('T','W','O','F','U','R')
digits = range(10)

# TWO + TWO = FOUR
def solve():
    for perm in itertools.permutations(digits, len(letters)):
        assign = dict(zip(letters, perm))

        # Leading digit cannot be zero
        if assign['T'] == 0 or assign['F'] == 0:
            continue  

        TWO  = assign['T']*100 + assign['W']*10 + assign['O']
        FOUR = assign['F']*1000 + assign['O']*100 + assign['U']*10 + assign['R']

        if TWO + TWO == FOUR:
            print("Solution Found!")
            print("TWO =", TWO)
            print("FOUR =", FOUR)
            print("\nAssignments:", assign)
            return

    print("No solution found.")

solve()
