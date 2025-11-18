from collections import deque

def water_jug():
    visited = set()
    queue = deque()

    # (jug5, jug7)
    queue.append((0, 0))
    visited.add((0, 0))

    while queue:
        x, y = queue.popleft()
        print("State:", (x, y))

        if y == 4:      # Target: 4 gallons in 7-gallon jug
            print("Goal Reached:", (x, y))
            return

        possible_states = set()

        # Fill jugs
        possible_states.add((5, y))   # Fill jug 1
        possible_states.add((x, 7))   # Fill jug 2

        # Empty jugs
        possible_states.add((0, y))   # Empty jug 1
        possible_states.add((x, 0))   # Empty jug 2

        # Pour jug1 → jug2
        pour = min(x, 7 - y)
        possible_states.add((x - pour, y + pour))

        # Pour jug2 → jug1
        pour = min(y, 5 - x)
        possible_states.add((x + pour, y - pour))

        for state in possible_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

water_jug()
