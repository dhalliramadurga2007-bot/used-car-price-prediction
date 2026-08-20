import pandas as pd
import numpy as np
import joblib

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from xgboost import XGBRegressor


# =========================================
# 1. LOAD DATA
# =========================================

train_data = pd.read_csv(
    "data/processed/used_car_train_processed.csv"
)

test_data = pd.read_csv(
    "data/processed/used_car_test_processed.csv"
)

print("Train shape:", train_data.shape)
print("Test shape :", test_data.shape)


# =========================================
# 2. TARGET COLUMN
# =========================================

target_column = "listed_price"

if target_column not in train_data.columns:
    print("\nERROR: Target column not found!")
    print("Available columns:")
    print(train_data.columns.tolist())
    exit()


# =========================================
# 3. SPLIT FEATURES AND TARGET
# =========================================

X_train = train_data.drop(columns=[target_column])
y_train = train_data[target_column]

X_test = test_data.drop(columns=[target_column])
y_test = test_data[target_column]


# =========================================
# 4. STORE RESULTS
# =========================================

results = []


def evaluate_model(name, model):

    print("\n====================================")
    print("Training:", name)
    print("====================================")

    # Train
    model.fit(X_train, y_train)

    # Predict
    predictions = model.predict(X_test)

    # Metrics
    mae = mean_absolute_error(
        y_test,
        predictions
    )

    rmse = np.sqrt(
        mean_squared_error(
            y_test,
            predictions
        )
    )

    r2 = r2_score(
        y_test,
        predictions
    )

    print("MAE :", mae)
    print("RMSE:", rmse)
    print("R2  :", r2)

    results.append({
        "Algorithm": name,
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    })

    return model


# =========================================
# 5. LINEAR REGRESSION
# =========================================

linear_model = LinearRegression()

evaluate_model(
    "Linear Regression",
    linear_model
)


# =========================================
# 6. RANDOM FOREST
# =========================================

random_forest = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

evaluate_model(
    "Random Forest",
    random_forest
)


# =========================================
# 7. XGBOOST
# =========================================

xgboost_model = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=6,
    random_state=42,
    n_jobs=-1
)

evaluate_model(
    "XGBoost",
    xgboost_model
)


# =========================================
# 8. COMPARISON TABLE
# =========================================

results_df = pd.DataFrame(results)

print("\n\n====================================")
print("MODEL COMPARISON")
print("====================================")

print(results_df)


# =========================================
# 9. FIND BEST MODEL
# =========================================

best_model = results_df.loc[
    results_df["R2"].idxmax()
]

print("\n====================================")
print("BEST MODEL")
print("====================================")

print(
    "Algorithm:",
    best_model["Algorithm"]
)

print(
    "MAE      :",
    best_model["MAE"]
)

print(
    "RMSE     :",
    best_model["RMSE"]
)

print(
    "R2 Score :",
    best_model["R2"]
)


# =========================================
# 10. SAVE RANDOM FOREST MODEL
# =========================================

joblib.dump(
    random_forest,
    "models/random_forest_model.pkl"
)

print("\n====================================")
print("MODEL SAVED SUCCESSFULLY")
print("====================================")

print(
    "File: models/random_forest_model.pkl"
)