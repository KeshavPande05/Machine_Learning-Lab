# Lab 1 — Functions
**Date:** 5 Jan 2026

---

## 🎯 Learning Goals

In this lab, you will learn about linear and nonlinear functions and their derivatives.

By the end of this lab, you should be able to:

1. Understand different types of functions that are useful for ML algorithms.
2. Know how they are implemented in standard Python libraries.

---

## 📝 Exercises

### 1. Matrix Multiplication (AᵀA)

Implement **AᵀA** where:

$$
A =
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
$$

---

### 2. Linear Function

Implement and plot:

$$
y = 2x_1 + 3
$$

**Range:** `start = -100, stop = 100, num = 100`

---

### 3. Quadratic Function

Implement and plot:

$$
y = 2x_1^2 + 3x_1 + 4
$$

**Range:** `start = -10, stop = 10, num = 100`

---

### 4. Gaussian PDF

Implement and plot the **Gaussian Probability Density Function**:

| Parameter | Value |
|-----------|-------|
| Mean (μ) | 0 |
| Standard Deviation (σ) | 15 |
| Range | `start = -100, stop = 100, num = 100` |

---

### 5. Derivative of a Function

Implement and plot:

$$
y = x_1^2
$$

**Range:** `start = -10, stop = 10, num = 100`

#### Tasks

- Compute the derivative at selected points.
- Find the value of $x_1$ where $y' = 0$.
- State what you infer from the result.

---

### 6. Multivariable Function & Gradient

Implement:

$$
y = 2x_1 + 3x_2 + 3x_3 + 4
$$

where $x_1$, $x_2$, $x_3$ are independent variables.

#### Tasks

- Compute the **gradient** of $y$.
- Evaluate the gradient at multiple points.
- Print the values.

---

## 7. Matrix Multiplication & Linear Model

### Problem Statement

Consider the linear model:

$$
y = 2x_1 + 3x_2 + 3x_3 + 4
$$

The coefficient vector is:

$$
\theta =
\begin{bmatrix}
2 \\
3 \\
3
\end{bmatrix}
$$

---

### Given Data

Matrix $X$ (5 samples, 3 features):

$$
X =
\begin{bmatrix}
1 & 0 & 2 \\
0 & 1 & 1 \\
2 & 1 & 0 \\
1 & 1 & 1 \\
0 & 2 & 1
\end{bmatrix}
$$

---

### Task

Compute:

$$
X\theta
$$
