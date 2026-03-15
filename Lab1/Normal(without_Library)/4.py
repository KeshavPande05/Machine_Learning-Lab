# Gaussian Implementation
#f(x) = (1 / (σ√(2π))) · exp(−½ · ((x − μ) / σ)²)
import math

sigma = 15
mean = 0
start = -100
end = 100
num = 100
step = (end - start) / num

x = []
for i in range(num + 1):
    x.append(start + i * step)  # fix 1

y = []
for xi in x:
    val = (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((xi - mean) / sigma) ** 2)  # fix 2
    y.append(val)

for i in range(len(x)):
    print(f"x = {x[i]:.2f}  y = {y[i]:.6f}")

import matplotlib.pyplot as plt

plt.plot(x, y)
plt.title('Gaussian PDF (mean=0, sigma=15)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

