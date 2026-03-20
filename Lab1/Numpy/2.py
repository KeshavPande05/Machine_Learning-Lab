# Implement y = 2x1 + 3 and plot using numpy and matplotlib

import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x1 = np.linspace(-100, 100, 100)

# Compute y
y = 2 * x1 + 3

# Plot
plt.figure()
plt.plot(x1, y)
plt.xlabel("x1")
plt.ylabel("y")
plt.title("Plot of y = 2x1 + 3")
plt.show()