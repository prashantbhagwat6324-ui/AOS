import heapq

# Manhattan Distance Heuristic
def heuristic(state, goal):
    distance = 0
    for i in range(1,9):
        x1, y1 = divmod(state.index(i), 3)
        x2, y2 = divmod(goal.index(i), 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

# Get next possible moves
def get_neighbors(state):
    neighbors = []
    idx = state.index(0)
    x, y = divmod(idx, 3)

    moves = {
        "up": (x-1, y),
        "down": (x+1, y),
        "left": (x, y-1),
        "right": (x, y+1)
    }

    for move, (nx, ny) in moves.items():
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_idx = nx * 3 + ny
            new_state = state[:]
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(new_state)
    return neighbors

# A* Search
def a_star(start, goal):
    pq = []
    heapq.heappush(pq, (0, start))
    visited = set()

    while pq:
        cost, state = heapq.heappop(pq)

        if state == goal:
            return state

        visited.add(tuple(state))

        for nbr in get_neighbors(state):
            if tuple(nbr) not in visited:
                total_cost = heuristic(nbr, goal)
                heapq.heappush(pq, (total_cost, nbr))

    return None


start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

result = a_star(start, goal)

print("Goal State Reached:")
print(result[0:3])
print(result[3:6])
print(result[6:9])
