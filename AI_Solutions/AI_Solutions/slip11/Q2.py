from collections import deque

def water_jug():
    visited = set()
    queue = deque()

    # state = (jug4, jug3)
    queue.append((0, 0))
    visited.add((0, 0))

    while queue:
        x, y = queue.popleft()   # x = 4L jug, y = 3L jug
        print("State:", (x, y))

        # Goal: 2 gallons in 3-liter jug
        if y == 2:
            print("\nGoal Reached:", (x, y))
            return

        possible_states = set()

        # Fill jugs
        possible_states.add((4, y))   # Fill 4L jug
        possible_states.add((x, 3))   # Fill 3L jug

        # Empty jugs
        possible_states.add((0, y))
        possible_states.add((x, 0))

        # Pour 4L → 3L
        pour = min(x, 3 - y)
        possible_states.add((x - pour, y + pour))

        # Pour 3L → 4L
        pour = min(y, 4 - x)
        possible_states.add((x + pour, y - pour))

        for state in possible_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

water_jug()
