import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read simulated Data csv file
data = pd.read_csv("simulated_data_multiple_linear_regression_for_ML.csv")
X = data.loc[:, 'age':'Gender'].values
y = data['disease_score'].values.reshape(-1, 1)

# Feature scaling
X_mean = X.mean(axis=0)
X_std = X.std(axis=0)
X_scaled = (X - X_mean) / X_std

# Adding intercept
X_scaled = np.hstack((np.ones((X_scaled.shape[0], 1)), X_scaled))


def hypothesis_func(X, theta):
    return np.dot(X, theta)


def cost_func(X, y, theta):
    m = len(y)
    hypothes = hypothesis_func(X, theta)
    cost = (1 / (2 * m)) * np.sum((hypothes - y) ** 2)
    return cost


def compute_gradient(X, y, theta):
    m = len(y)
    hypoth = hypothesis_func(X, theta)
    derivat = np.zeros_like(theta)

    for i in range(m):
        for j in range(X.shape[1]):
            derivat[j] += (hypoth[i] - y[i]) * X[i, j]

    derivat = derivat / m
    return derivat

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def r2_score(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred)**2)
    ss_tot = np.sum((y_true - np.mean(y_true))**2)
    return 1 - (ss_res / ss_tot)


def main():
    theta = np.zeros((X_scaled.shape[1], 1))

    learning_rate = 0.01
    num_of_iterations = 1000
    cost_history = []

    for i in range(num_of_iterations):
        gradient = compute_gradient(X_scaled, y, theta)
        theta -= learning_rate * gradient
        cost = cost_func(X_scaled, y, theta)
        cost_history.append(cost)

        print(f"Iteration-{i}: cost = {cost}, parameters = {theta}")

    print(theta)
    y_pred = hypothesis_func(X_scaled, theta)
    # Plot convergence
    plt.plot(range(num_of_iterations), cost_history)
    plt.title("Convergence plot")
    plt.xlabel("No. of iterations")
    plt.ylabel("Cost")

    plt.savefig("convergence.png")
    print("\nMSE :", mse(y, y_pred))
    print("R²  :", r2_score(y, y_pred))

if __name__ == "__main__":
    main()