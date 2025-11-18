import itertools

letters = ('C','R','O','S','A','D','N','G','E')
digits = range(10)

for perm in itertools.permutations(digits, len(letters)):
    C,R,O,S,A,D,N,G,E = perm

    # No leading zeros
    if C == 0 or R == 0 or D == 0:
        continue

    CROSS = C*10000 + R*1000 + O*100 + S*10 + S
    ROADS = R*10000 + O*1000 + A*100 + D*10 + S
    DANGER = D*100000 + A*10000 + N*1000 + G*100 + E*10 + R

    if CROSS + ROADS == DANGER:
        print("Solution Found:")
        print(f"C={C}, R={R}, O={O}, S={S}, A={A}, D={D}, N={N}, G={G}, E={E}")
        print(f"{CROSS} + {ROADS} = {DANGER}")
        break
else:
    print("No solution found.")
