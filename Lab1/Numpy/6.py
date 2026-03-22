# Implement y = 2x1 + 3x2 + 3x3 + 4, where x1, x2 and x3 are three independent variables.
# Compute the gradient of y at a few points and print the values.

import numpy as np


def compute_y_and_gradient(x1, x2, x3):
    # Function implementation
    y = 2 * x1 + 3 * x2 + 3 * x3 + 4

    # Gradient calculation: [dy/dx1, dy/dx2, dy/dx3]
    # Since the function is linear, the gradient is constant.
    gradient = np.array([2, 3, 3])

    return y, gradient


# Points for evaluation
test_points = [(0, 0, 0), (1, 2, 3), (-1, 0, 5), (10, -5, 2)]

for p in test_points:
    val, grad = compute_y_and_gradient(*p)
    print(f"Point {p}: y = {val}, Gradient = {grad}")
