graph = {
    1: [2, 3, 4],
    2: [1, 4, 5],
    3: [1, 4],
    4: [1, 2, 3, 7],
    5: [2, 6, 7],
    6: [5, 7],
    7: [4, 5, 6]
}

visited = []

def dfs(node, goal):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        if node == goal:
            return True

        for nbr in graph[node]:
            if dfs(nbr, goal):
                return True
    return False

print("DFS Traversal (Start=2):")
dfs(2, 7)
print("\nGoal Found:", 7)
