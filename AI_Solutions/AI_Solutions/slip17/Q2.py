import heapq

def a_star(start, goal):
    pq = []
    heapq.heappush(pq, (heuristic[start], 0, start, [start]))  # (f(n), g(n), node, path)
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


graph = {
    'A': {'B': 9, 'C': 4, 'D': 7},
    'B': {'E': 11},
    'C': {'E': 17, 'F': 12},
    'D': {'F': 14},
    'E': {'G': 5},
    'F': {'G': 9},
    'G': {}
}

heuristic = {
    'A': 21,
    'B': 14,
    'C': 18,
    'D': 18,
    'E': 5,
    'F': 8,
    'G': 0
}

path, cost = a_star('A', 'G')

print("Best Path:", path)
print("Total Cost:", cost)
