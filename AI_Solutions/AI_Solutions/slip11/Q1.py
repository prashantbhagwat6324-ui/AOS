def mea_transform(start, goal):
    print("Start String:", start)
    print("Goal String:", goal)
    print("\nSteps using Means-End Analysis:\n")

    i, j = 0, 0

    while i < len(start) or j < len(goal):

        # If both positions valid and characters match → move ahead
        if i < len(start) and j < len(goal) and start[i] == goal[j]:
            print(f"Match: '{start[i]}' → No change")
            i += 1
            j += 1

        # Replace if both present but different
        elif i < len(start) and j < len(goal):
            print(f"Replace '{start[i]}' with '{goal[j]}'")
            i += 1
            j += 1

        # Insert char (goal has extra character)
        elif j < len(goal):
            print(f"Insert '{goal[j]}'")
            j += 1

        # Delete char (start has extra character)
        elif i < len(start):
            print(f"Delete '{start[i]}'")
            i += 1


# Example input
start = "cat"
goal = "smart"

mea_transform(start, goal)
