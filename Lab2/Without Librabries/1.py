# Original data
from statistics import mean

X = [
    [1, 0, 2],
    [0, 1, 1],
    [2, 1, 0],
    [1, 1, 1],
    [0, 2, 1]
]

n = len(X)
print(n)
d = len(X[0])
print(d)
mean=[0]*d

# Original data
X = [
    [1, 0, 2],
    #[0,0],[0,1],[0,2]
    [0, 1, 1],
    #[1,0],[1,1],[1,2]
    [2, 1, 0],
    [1, 1, 1],
    [0, 2, 1]
]

n = len(X)  # no of rows
d = len(X[0]) # no of columns

# X = 5 X 3
# step1 = compute the mean of each column and store it

Mean = [0] * d
for i in range(d):
    for j in range(n):
        mean[i] += X[j][i]
    mean[i] /= n
    print(mean)

# step 2 :-
Xc =[]
for i in range(n):
    row = []
    for j in range(d):
        row.append(X[i][j] - mean[j])
    Xc.append(row)
    print(Xc)

 # Step 3: Compute covariance matrix
cov = [[0 for _ in range(d)] for _ in range(d)]

for i in range(d):
    for j in range(d):
        s = 0
        for k in range(n):
            s += Xc[k][i] * Xc[k][j]
        cov[i][j] = s / (n - 1)

# Print result
for row in cov:
    print(row)