graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8],
    5: [8],
    6: [8],
    7: [8],
    8: []
}

visited = []

def dfs(node, goal):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        if node == goal:
            return True
        
        for neighbor in graph[node]:
            if dfs(neighbor, goal):
                return True
    return False


start = 1
goal = 8

print("DFS Traversal:")
dfs(start, goal)
print("\nGoal Found:", goal)
