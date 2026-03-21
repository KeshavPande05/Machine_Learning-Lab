# Implement y = 2x1^2 + 3 and plot using numpy and matplotlib

import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x1 = np.linspace(-10, 10, 100)

# Compute y
y = 2 *x1**2 + 3*x1 +4

# Plot
plt.figure()
plt.plot(x1, y)
plt.xlabel("x1")
plt.ylabel("y")
plt.title("Plot of y = 2x² + 3x + 4'")
plt.show()