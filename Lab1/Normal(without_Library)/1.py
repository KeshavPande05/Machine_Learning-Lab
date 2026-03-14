# IMPLEMENT AᵀA - A = [[1 2 3 ][ 4 5 6]]
from unittest import result

from talloc import total_blocks

A = [[1, 2, 3],
     [4, 5, 6]]

# Basic
# A[0]  →  [1, 2, 3]   → len = 3
# A[1]  →  [4, 5, 6]   → len = 3

# A is 2x3 → rows=2, cols=3
rows = len(A)        # 2
cols = len(A[0])     # 3

# Step 1: Transpose
AT = []
for col in range(cols):
    new_row = []
    for row in range(rows):
        new_row.append(A[row][col])
    AT.append(new_row)

# Step 2: AᵀA
AT_A = [[0] * cols for _ in range(cols)]

for i in range(len(AT)):
    for j in range(len(A[0])):
        for k in range(len(A)):
            AT_A[i][j] += AT[i][k] * A[k][j]

# Print
print("AT_A:")
for row in AT_A:
    print(row)




