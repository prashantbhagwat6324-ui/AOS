from collections import deque

graph = {
    1: [2, 3, 4],
    2: [1, 4, 5],
    3: [1, 4],
    4: [1, 2, 3, 7],
    5: [2, 6, 7],
    6: [5, 7],
    7: [4, 5, 6]
}

def bfs(start, goal):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            if node == goal:
                return True

            for nbr in graph[node]:
                queue.append(nbr)
    
    return False

print("BFS Traversal:")
found = bfs(1, 7)
print("\nGoal Found:", found)
