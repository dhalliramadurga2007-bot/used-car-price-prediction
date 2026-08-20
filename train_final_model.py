import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from xgboost import XGBRegressor


# ============================================================
# 1. LOAD DATASET
# ============================================================

df = pd.read_csv("data/raw/cars_data_clean.csv")

print("Dataset loaded!")
print("Original shape:", df.shape)


# ============================================================
# 2. FEATURES USED IN STREAMLIT APP
# ============================================================

features = [
    "oem",
    "model",
    "myear",
    "body",
    "transmission",
    "fuel",
    "km",
    "Seats"
]

target = "listed_price"


# ============================================================
# 3. KEEP REQUIRED COLUMNS
# ============================================================

df = df[features + [target]].copy()


# ============================================================
# 4. CLEAN TARGET COLUMN
# ============================================================

df[target] = pd.to_numeric(
    df[target],
    errors="coerce"
)

df = df.dropna(
    subset=[target]
)

# Remove zero / negative prices
df = df[df[target] > 0].copy()


# ============================================================
# 5. CLEAN CATEGORICAL FEATURES
# ============================================================

categorical_features = [
    "oem",
    "model",
    "body",
    "transmission",
    "fuel"
]

for col in categorical_features:

    df[col] = df[col].astype("string")

    df[col] = df[col].fillna("Unknown")

    df[col] = df[col].str.strip()

    df.loc[
        df[col] == "",
        col
    ] = "Unknown"


# ============================================================
# 6. CLEAN NUMERIC FEATURES
# ============================================================

numeric_features = [
    "myear",
    "km",
    "Seats"
]

for col in numeric_features:

    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

    median_value = df[col].median()

    df[col] = df[col].fillna(
        median_value
    )


# ============================================================
# 7. REMOVE EXTREME PRICE OUTLIERS
# ============================================================

lower_limit = df[target].quantile(0.01)
upper_limit = df[target].quantile(0.99)

print("\nPrice limits used:")
print("1st percentile :", lower_limit)
print("99th percentile:", upper_limit)

df = df[
    (df[target] >= lower_limit) &
    (df[target] <= upper_limit)
].copy()

print("\nShape after cleaning:", df.shape)


# ============================================================
# 8. CREATE LOG TARGET
# ============================================================

df["log_price"] = np.log1p(
    df[target]
)


# ============================================================
# 9. SPLIT FEATURES AND TARGET
# ============================================================

X = df[features].copy()

y = df["log_price"].copy()


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTrain rows:", len(X_train))
print("Test rows :", len(X_test))


# ============================================================
# 10. PREPROCESSOR
# ============================================================

preprocessor = ColumnTransformer(
    transformers=[

        (
            "categorical",
            OneHotEncoder(
                handle_unknown="ignore",
                sparse_output=True
            ),
            categorical_features
        ),

        (
            "numeric",
            StandardScaler(),
            numeric_features
        )
    ]
)


# ============================================================
# 11. MODELS
# ============================================================

models = {

    "Linear Regression":
        LinearRegression(),

    "Random Forest":
        RandomForestRegressor(
            n_estimators=200,
            max_depth=None,
            min_samples_split=2,
            min_samples_leaf=1,
            random_state=42,
            n_jobs=-1
        ),

    "XGBoost":
        XGBRegressor(
            n_estimators=500,
            learning_rate=0.05,
            max_depth=6,
            subsample=0.9,
            colsample_bytree=0.9,
            objective="reg:squarederror",
            random_state=42,
            n_jobs=-1
        )
}


# ============================================================
# 12. RESULTS STORAGE
# ============================================================

results = []

trained_pipelines = {}

best_pipeline = None
best_model_name = None

best_r2 = float("-inf")


# ============================================================
# 13. TRAIN AND EVALUATE MODELS
# ============================================================

for name, model in models.items():

    print("\n========================================")
    print("Training:", name)
    print("========================================")

    pipeline = Pipeline(
        steps=[
            (
                "preprocessor",
                preprocessor
            ),
            (
                "model",
                model
            )
        ]
    )

    # Train on log-price
    pipeline.fit(
        X_train,
        y_train
    )

    # Predict log-price
    log_predictions = pipeline.predict(
        X_test
    )

    # Convert predictions back to rupees
    predictions = np.expm1(
        log_predictions
    )

    # Convert actual y_test back to rupees
    actual_prices = np.expm1(
        y_test.to_numpy()
    )

    # Prevent negative predicted prices
    predictions = np.maximum(
        predictions,
        0
    )

    # Metrics
    mae = mean_absolute_error(
        actual_prices,
        predictions
    )

    rmse = np.sqrt(
        mean_squared_error(
            actual_prices,
            predictions
        )
    )

    r2 = r2_score(
        actual_prices,
        predictions
    )

    print("MAE :", mae)
    print("RMSE:", rmse)
    print("R2  :", r2)

    results.append(
        {
            "Algorithm": name,
            "MAE": mae,
            "RMSE": rmse,
            "R2": r2
        }
    )

    trained_pipelines[name] = pipeline

    # Select best model using highest R2
    if r2 > best_r2:

        best_r2 = r2

        best_model_name = name

        best_pipeline = pipeline


# ============================================================
# 14. COMPARISON TABLE
# ============================================================

results_df = pd.DataFrame(
    results
)

results_df = results_df.sort_values(
    by="R2",
    ascending=False
).reset_index(drop=True)

print("\n\n========================================")
print("MODEL COMPARISON")
print("========================================")

print(
    results_df.to_string(
        index=False
    )
)


# ============================================================
# 15. BEST MODEL DETAILS
# ============================================================

best_result = results_df.iloc[0]

print("\n========================================")
print("BEST MODEL")
print("========================================")

print(
    "Algorithm:",
    best_result["Algorithm"]
)

print(
    "MAE      :",
    best_result["MAE"]
)

print(
    "RMSE     :",
    best_result["RMSE"]
)

print(
    "R2 Score :",
    best_result["R2"]
)


# ============================================================
# 16. SAVE BEST MODEL PIPELINE
# ============================================================

joblib.dump(
    best_pipeline,
    "models/final_app_model.pkl"
)


# ============================================================
# 17. SAVE MODEL INFO
# ============================================================

model_info = {
    "features": features,
    "categorical_features": categorical_features,
    "numeric_features": numeric_features,
    "target": target,
    "target_transform": "log1p",
    "best_model": best_model_name,
    "best_r2": float(best_result["R2"]),
    "best_mae": float(best_result["MAE"]),
    "best_rmse": float(best_result["RMSE"]),
    "price_lower_limit": float(lower_limit),
    "price_upper_limit": float(upper_limit)
}

joblib.dump(
    model_info,
    "models/final_app_model_info.pkl"
)


# ============================================================
# 18. SAVE COMPARISON RESULTS
# ============================================================

results_df.to_csv(
    "results/final_model_comparison.csv",
    index=False
)


print("\n========================================")
print("FILES SAVED SUCCESSFULLY")
print("========================================")

print(
    "Model : models/final_app_model.pkl"
)

print(
    "Info  : models/final_app_model_info.pkl"
)

print(
    "Results: results/final_model_comparison.csv"
)