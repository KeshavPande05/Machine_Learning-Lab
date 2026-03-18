# IMPLEMENT AᵀA - A = [[1 2 3 ][ 4 5 6]]
import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Transpose
AT = A.T

Result = AT @ A
print(Result)

