from collections import deque

# States:
# (monkey_position, box_position, monkey_on_box, has_banana)

def monkey_banana():
    start = ("door", "window", False, False)
    goal = ("middle", "middle", True, True)

    queue = deque([start])
    visited = set([start])

    while queue:
        state = queue.popleft()
        print("Current State:", state)

        monkey, box, on_box, banana = state

        if banana:
            print("\nGoal Reached:", state)
            return

        next_states = []

        # 1. Monkey walks independently
        if not on_box:
            for pos in ["door", "window", "middle"]:
                if pos != monkey:
                    next_states.append((pos, box, on_box, banana))

        # 2. Push box (only if monkey and box at same location)
        if monkey == box and not on_box:
            for pos in ["door", "window", "middle"]:
                if pos != box:
                    next_states.append((pos, pos, on_box, banana))

        # 3. Monkey climbs box
        if monkey == box and not on_box:
            next_states.append((monkey, box, True, banana))

        # 4. Monkey grabs banana (only when on box at "middle")
        if on_box and monkey == "middle":
            next_states.append((monkey, box, on_box, True))

        # Add new states to queue
        for ns in next_states:
            if ns not in visited:
                visited.add(ns)
                queue.append(ns)


monkey_banana()
