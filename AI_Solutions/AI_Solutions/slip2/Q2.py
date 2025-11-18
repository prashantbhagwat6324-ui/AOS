graph = {
    1: [3, 2],
    3: [2],
    2: [4],
    4: [6, 5],     # 4 → 6 and 4 → 5
    5: [3, 7],     # 5 → 3 and 5 → 7
    7: [6],        # 7 → 6
    6: []
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

print("DFS Traversal:")
found = dfs(1, 7)
print("\nGoal Found:", found)
