def dfs_limited(node, goal, depth):
    if depth == 0:
        return node == goal

    print(node, end=" ")

    for child in graph[node]:
        if dfs_limited(child, goal, depth - 1):
            return True

    return False


def iddfs(start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nDepth Limit = {depth}:")
        if dfs_limited(start, goal, depth):
            print(f"\nGoal Found at depth {depth}")
            return True

    print("\nGoal Not Found")
    return False


# YOUR GRAPH
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': [],
    'F': ['K'],
    'G': [],
    'H': [],
    'I': [],
    'K': []
}

iddfs('A', 'G', 5)
