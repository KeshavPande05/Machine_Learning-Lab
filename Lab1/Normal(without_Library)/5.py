# Implement y = x1^2, plot x1, y in the range [start=--10, stop=10, num=100]. Compute the
# value of derivatives at these points, x1 = -5, -3, 0, 3, 5. What is the value of x1 at which
# the function value (y) is zero. What do you infer from this?

import numpy as np
import matplotlib.pyplot as plt

start, end, num = -10, 10, 100
step = (end - start) / num

x = []
for i in range(num + 1):
    x.append(start + i * step)


y = []
for xi in x:
    y.append(xi**2)


dy = []
for i in range(len(x)):

    if i == 0:   # forward difference
        dy.append((y[1] - y[0]) / step)

    elif i == len(x) - 1:   # backward difference
        dy.append((y[-1] - y[-2]) / step)

    else:   # central difference
        dy.append((y[i+1] - y[i-1]) / (2 * step))


points = [-5, -3, 0, 3, 5]

print("Derivative at given points:\n")

for p in points:
    idx = min(range(len(x)), key=lambda i: abs(x[i] - p))

    numerical = dy[idx]
    analytical = 2 * p

    print(f"x = {p:>3}  Numerical = {numerical:.4f}  Analytical = {analytical}")


print("\nx where y ≈ 0:\n")

for i in range(len(y)):
    if abs(y[i]) < 0.01:
        print(f"x = {x[i]:.2f}   y = {y[i]:.6f}")


plt.figure(figsize=(8,5))

plt.plot(x, y, label="y = x^2")
plt.plot(x, dy, label="dy/dx (numerical)", linestyle="--")

plt.xlabel("x")
plt.ylabel("Value")
plt.title("Function and Numerical Derivative")

plt.legend()
plt.grid()

plt.show()