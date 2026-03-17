# Numpy  = fast array + maths Operation
# List = slow

# Creating a arrays
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])
print(a)
print(b)
print(c)

# Key difference from List it can be added or subract and multiply
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))
print(np.true_divide(a,b))

# step for 2D arrays(matrices)
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
# Access elements
print(A[0])     # first row
print(A[0][1])  # element = 2

# Step :- Important Functions
#Zeroes
A=np.zeros((2,3))
print(A)

#Ones
B=np.ones((2,3))
print(B)


#Shape of matrix
print(a.shape)

# Linearly spaced
print(np.linspace(0,10,5))

# Vectorization
result = a *2
print(result)

# Matrix Multiplication
import numpy as np

x = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

theta = np.array([1, 2, 3])
result = np.dot(x, theta)
print(result)

# Reshapr
a = np.array([1,2,3,4])
a.reshape(2,2)

# Mean , sum , max
a = np.array([1,2,3])

print(a.mean())
print(a.sum())
print(a.max())

# Broadcasting
a = np.array([1,2,3])
print(a + 5)

