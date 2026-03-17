import numpy as np
theta = [2,3,3]
X = [ [1,0,2],[0,1,1],[2,1,0],[1,1,1],[0,2,1]]

y1 = len(theta)
x1 = len(X)
x2= len(X[0])

A =[]
for i in X :
    sum_val = 0
    for j in range(len(theta)):
        sum_val += i[j] * theta[j]
    A.append(sum_val)

print(A)
