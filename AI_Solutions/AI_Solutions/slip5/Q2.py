from collections import deque

graph = {
    1: [2, 4],
    2: [3],
    3: [4, 5, 6],
    4: [2],        # updated
    5: [7, 8],
    6: [8],
    7: [8],
    8: []
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
found = bfs(1, 8)
print("\nGoal Found:", found)
