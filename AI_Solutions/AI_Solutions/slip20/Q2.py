def minmax(depth, nodeIndex, isMax, scores, height):
    if depth == height:
        return scores[nodeIndex]

    if isMax:
        return max(
            minmax(depth + 1, nodeIndex * 2, False, scores, height),
            minmax(depth + 1, nodeIndex * 2 + 1, False, scores, height)
        )
    else:
        return min(
            minmax(depth + 1, nodeIndex * 2, True, scores, height),
            minmax(depth + 1, nodeIndex * 2 + 1, True, scores, height)
        )

scores = [3, 5, 2, 9, 12, 5, 23, 23]
height = 3

print("The optimal value is:", minmax(0, 0, True, scores, height))
