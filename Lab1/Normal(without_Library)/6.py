# Implement y = 2x1 + 3x2 + 3x3 + 4, where x1, x2 and x3 are three independent variables.
# Compute the gradient of y at a few points and print the values.

import numpy as np
def compute_y (x):
    x1, x2 ,x3 = x
    return 2*x1 + 3*x2 +3*x3 +4

def compute_gradient(x):
    dy_dx1 = 2
    dy_dx2 = 3
    dy_dx3 = 3
    return np.array([dy_dx1, dy_dx2, dy_dx3])

points =[
    [1,2,3],
    [4,5,6],
    [7,8,9]]

for p in points:
    y_vals = compute_y(p)
    grad = compute_gradient(p)
    print(f"\nPoint(x1,x2,x3 = {p}    y ={y_vals}    grad = {grad})")

