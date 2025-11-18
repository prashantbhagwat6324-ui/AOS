import heapq

goal_state = "123456780"

moves = {
    0: [1,3],        # possible moves of blank tile
    1: [0,2,4],
    2: [1,5],
    3: [0,4,6],
    4: [1,3,5,7],
    5: [2,4,8],
    6: [3,7],
    7: [4,6,8],
    8: [5,7]
}

def manhattan(state):
    dist = 0
    for i, ch in enumerate(state):
        if ch != '0':
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(int(ch)-1, 3)
            dist += abs(x1 - x2) + abs(y1 - y2)
    return dist

def a_star(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start))

    visited = {}
    visited[start] = None

    cost = {start: 0}

    while pq:
        f, g, state = heapq.heappop(pq)

        if state == goal_state:
            return reconstruct_path(visited, state)

        blank = state.index('0')

        for mv in moves[blank]:
            new_state = list(state)
            new_state[blank], new_state[mv] = new_state[mv], new_state[blank]
            new_state = "".join(new_state)

            new_cost = g + 1

            if new_state not in cost or new_cost < cost[new_state]:
                cost[new_state] = new_cost
                priority = new_cost + manhattan(new_state)
                heapq.heappush(pq, (priority, new_cost, new_state))
                visited[new_state] = state

    return None

def reconstruct_path(visited, state):
    path = []
    while state is not None:
        path.append(state)
        state = visited[state]
    return path[::-1]


start = input("Enter start state (9 digits, use 0 for blank): ")
result = a_star(start)

print("\nSolution Path:")
for step in result:
    print(step[0:3])
    print(step[3:6])
    print(step[6:9])
    print()
