from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import pandas as pd



# load Data
def load_data(filepath):
    data = pd.read_csv(filepath)
    X = data.loc[:, 'age':'Gender']
    y = data['disease_score']
    return X, y


# Split data set ( 30% test and 70 % train)
def split_and_scale(X, y, test_size=0.30, random_state=999):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled  = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler


# Train model
def train_model(X_train_scaled, y_train):
    print("-----TRAINING----")
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)
    return model


# Test MOdel
def evaluate_model(model, X_test_scaled, y_test):
    y_pred = model.predict(X_test_scaled)

    print("Predicted 'y' values are:")
    print(y_pred)

    r2  = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    print("r2 score (target = disease_score_fluct) is %0.2f" % r2)
    print(f"Mean squared error: {mse}")
    print("Successfully done!")
    return y_pred, r2, mse




# Print Theta values
def print_coefficients(model, feature_names):
    print(f"Intercept (θ₀): {model.intercept_:.4f}")
    print("Feature coefficients:")
    for name, coef in zip(feature_names, model.coef_):
        print(f"  {name:15}: {coef:+.4f}")

if __name__ == "__main__":
    X, y = load_data("simulated_data_multiple_linear_regression_for_ML.csv")

    X_train_scaled, X_test_scaled, y_train, y_test, scaler = split_and_scale(X, y)

    model = train_model(X_train_scaled, y_train)

    y_pred, r2, mse = evaluate_model(model, X_test_scaled, y_test)


    print_coefficients(model, X.columns)