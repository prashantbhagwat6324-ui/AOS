def f(x):
    return -x**2 + 4*x   # The function to maximize

def hill_climbing(start, step=0.1):
    current = start
    current_value = f(current)

    while True:
        # Try going left and right
        left = current - step
        right = current + step

        best = current
        best_value = current_value

        if f(left) > best_value:
            best = left
            best_value = f(left)

        if f(right) > best_value:
            best = right
            best_value = f(right)

        # If no improvement → reached peak
        if best == current:
            break

        current = best
        current_value = best_value

    return current, current_value


start_position = 0
maximum_x, maximum_value = hill_climbing(start_position)

print("Maximum at x =", maximum_x)
print("Maximum value =", maximum_value)
