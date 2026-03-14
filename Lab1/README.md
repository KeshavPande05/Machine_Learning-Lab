# Lab 1 - Functions - 5 Jan 2026

## Learning Goals

In this lab, you will learn linear and nonlinear functions and their derivatives.

By the end of this lab, you should be able to:
1. Understand different types of functions that are useful for ML algorithms.
2. How exactly they are implemented in standard python libraries

---

## Exercises

### 1. Matrix Multiplication (AᵀA)

Implement **AᵀA** where:

```
A = [[1, 2, 3],
     [4, 5, 6]]
```

---

### 2. Linear Function

Implement and plot:

$$y = 2x_1 + 3$$

- Range: `start=-100, stop=100, num=100`

---

### 3. Quadratic Function

Implement and plot:

$$y = 2x_1^2 + 3x_1 + 4$$

- Range: `start=-10, stop=10, num=100`

---

### 4. Gaussian PDF

Implement and plot the **Gaussian Probability Density Function** with:
- `mean = 0`
- `sigma = 15`
- Range: `start=-100, stop=100, num=100`

---

### 5. Derivative of a Function

Implement and plot:

$$y = x_1^2$$

- Range: `start=-10, stop=10, num=100`

**Tasks:**
- Compute the value of the derivative at: `x₁ = -5, -3, 0, 3, 5`
- Find the value of `x₁` at which the function value (`y`) is zero
- What do you infer from this?

---

### 6. Multivariable Function & Gradient

Implement:

$$y = 2x_1 + 3x_2 + 3x_3 + 4$$

where `x₁`, `x₂`, and `x₃` are three independent variables.

**Tasks:**
- Compute the **gradient** of `y` at a few points
- Print the values
