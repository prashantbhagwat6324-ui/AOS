import random

# Function
def f(x):
    return -x**2 + 4*x

# Hill Climbing Algorithm
def hill_climbing():
    current_x = 0     # fixed start for stable output
    step = 0.1

    while True:
        left_x = current_x - step
        right_x = current_x + step

        current_val = f(current_x)
        left_val = f(left_x)
        right_val = f(right_x)

        if left_val > current_val:
            current_x = left_x
        elif right_val > current_val:
            current_x = right_x
        else:
            break

    return current_x, f(current_x)

max_x, max_val = hill_climbing()
print("Maximum occurs at x =", round(max_x, 3))
print("Maximum value =", round(max_val, 3))
