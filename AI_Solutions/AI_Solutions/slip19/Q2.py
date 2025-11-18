import heapq

graph = {
    'A': {'B': 2, 'E': 3},
    'B': {'C': 1, 'F': 9},
    'E': {'D': 6},
    'D': {'F': 1},
    'C': {},
    'F': {}
}

heuristic = {
    'A': 11,
    'B': 6,
    'C': 99,
    'D': 1,
    'E': 7,
    'F': 0
}

def a_star(start, goal):
    pq = []
    heapq.heappush(pq, (heuristic[start], 0, start, [start]))  # (f,g,node,path)
    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            return path, g

        if node in visited:
            continue
        visited.add(node)

        for nbr, cost in graph[node].items():
            new_g = g + cost
            new_f = new_g + heuristic[nbr]
            heapq.heappush(pq, (new_f, new_g, nbr, path + [nbr]))

    return None, None


path, cost = a_star('A', 'F')

print("Best Path:", path)
print("Total Cost:", cost)
