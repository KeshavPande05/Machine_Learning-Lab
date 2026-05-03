# Lab 3 — Linear Regression

**Date:** 12 Jan 2026  
**Dataset:** `simulated_data_multiple_linear_regression_for_ML.csv`

---

## Learning Goals

By the end of this lab you should be able to:

1. Fit a linear model to real-world clinical data
2. Use scikit-learn for preprocessing, training, and evaluation
3. Implement linear regression from scratch using gradient descent

---

## Repository Structure

```
lab3/
│
├── simulated_data_multiple_linear_regression_for_ML.csv   # Dataset
│
├── linear_regression_sklearn.py       # Exercises 1 & 2 (scikit-learn)
├── linear_regression_from_scratch.py  # Exercise 3 (pure NumPy / gradient descent)
│
└── README.md
```

---

## Exercises

### Exercise 1 — Predict `disease_score` (scikit-learn)

**File:** `linear_regression_sklearn.py`

Uses `sklearn.linear_model.LinearRegression` with `StandardScaler` preprocessing.

**Pipeline:**
1. Load CSV → identify feature columns (everything except both target columns)
2. Train / test split (80 / 20, `random_state=42`)
3. Z-score normalisation with `StandardScaler` (fit on train, transform both)
4. Fit `LinearRegression` on the training set
5. Evaluate with **MSE** and **R²** on both train and test sets
6. Plot *Actual vs Predicted* and *Residuals*

**Run:**
```bash
python linear_regression_sklearn.py
```

---

### Exercise 2 — Predict `disease_score_fluct` (scikit-learn)

**File:** `linear_regression_sklearn.py` *(same script, second call)*

Identical pipeline to Exercise 1 but targeting `disease_score_fluct`.  
Because this target includes random fluctuation, a lower R² is expected — the
residual plot will reveal heteroscedasticity if fluctuation is not explained by
the features.

---

### Exercise 3 — Linear Regression from Scratch

**File:** `linear_regression_from_scratch.py`

Implements the full gradient descent loop using only NumPy.

#### Key Functions

| Function | Purpose |
|---|---|
| `load_data(filepath)` | Read the CSV with pandas |
| `prepare_xy(df, target_col)` | Extract X (with bias), y; apply z-score normalisation |
| `hypothesis(X, theta)` | Compute **h_θ(X) = X · θ** |
| `compute_cost(X, y, theta)` | Compute **J(θ) = (1/2m) Σ(h − y)²** |
| `compute_gradient(X, y, theta)` | Compute **∇J = (1/m) Xᵀ(Xθ − y)** |
| `gradient_descent(X, y, α, iters)` | Update **θ := θ − α ∇J** for `iters` steps |

#### Gradient Descent Update Rule

```
for each iteration:
    h      = X · θ              # hypothesis
    error  = h − y              # residuals
    grad   = (1/m) Xᵀ · error  # gradient
    θ      = θ − α · grad       # parameter update
```

#### Hyperparameters (defaults)

| Hyperparameter | Value |
|---|---|
| Learning rate α | 0.05 |
| Iterations | 2 000 |
| θ initialisation | zeros |

**Run:**
```bash
python linear_regression_from_scratch.py
```

---

## Mathematical Background

### Linear Hypothesis
$$h_\theta(x) = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \cdots + \theta_n x_n = \mathbf{x}^\top \boldsymbol{\theta}$$

### Cost Function (MSE / 2)
$$J(\boldsymbol{\theta}) = \frac{1}{2m} \sum_{i=1}^{m} \left( h_\theta(x^{(i)}) - y^{(i)} \right)^2$$

### Gradient
$$\frac{\partial J}{\partial \theta_j} = \frac{1}{m} \sum_{i=1}^{m} \left( h_\theta(x^{(i)}) - y^{(i)} \right) x_j^{(i)}$$

### Parameter Update
$$\theta_j := \theta_j - \alpha \frac{\partial J}{\partial \theta_j}$$

---

## Results Interpretation

| Metric | Meaning |
|---|---|
| **R²** | Fraction of variance explained. 1.0 = perfect, 0 = predicts mean |
| **MSE** | Average squared error. Lower is better |
| **Residual plot** | Should be random around 0 for a good linear fit |
| **Learning curve** | Cost should decrease and plateau (no divergence) |

A high R² for `disease_score` and a noticeably lower R² for `disease_score_fluct`
is expected — the fluctuation target contains random noise that no linear model
can capture.

---

## Dependencies

```
numpy
pandas
matplotlib
scikit-learn
```

Install with:
```bash
pip install numpy pandas matplotlib scikit-learn
```
