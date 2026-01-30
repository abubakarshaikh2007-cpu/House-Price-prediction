# =========================
# HOUSE PRICE PREDICTION
# Linear Regression
# =========================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("house_price.csv")

# =========================
# DATA CLEANING
# =========================
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

# =========================
# FEATURES & TARGET
# =========================
X = df[["area", "bedrooms", "bathrooms"]]
y = df["price"]

# =========================
# TRAIN TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# =========================
# MODEL TRAINING
# =========================
model = LinearRegression()
model.fit(X_train, y_train)

# =========================
# MODEL DETAILS
# =========================
print("Weights:", model.coef_)
print("Intercept:", model.intercept_)

# =========================
# PREDICTION (NEW HOUSE)
# =========================
new_house = [[1600, 3, 2]]
predicted_price = model.predict(new_house)

print("Predicted House Price:", predicted_price[0])

# =========================
# MODEL EVALUATION
# =========================
y_pred = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))