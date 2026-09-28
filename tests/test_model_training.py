
import pandas as pd
import joblib
from sklearn.base import clone

DATASET_PATH = "Integrated_Cleaned_Dataset_with_Revenue.csv"
MODEL_PATH = "best_model.pkl"

FEATURES = [
    "quantity",
    "unit_price",
    "year",
    "month",
    "day",
    "product",
    "region",
    "weekday",
    "time_of_day",
    "product_category"
]

TARGET = "revenue"


def test_model_training():
    # Load a tiny sample so CI stays fast and cheap
    df = pd.read_csv(
        DATASET_PATH,
        nrows=500,
        low_memory=False
    )

    X = df[FEATURES]
    y = df[TARGET]

    # Load the existing pipeline only to obtain its architecture
    original_model = joblib.load(MODEL_PATH)

    # Create a fresh, untrained model
    model = clone(original_model)

    # ACTUAL TRAINING
    model.fit(X, y)

    # Verify that preprocessing was fitted
    assert hasattr(
        model.named_steps["preprocessor"],
        "transformers_"
    )

    # Verify that LinearRegression actually learned parameters
    assert hasattr(
        model.named_steps["model"],
        "coef_"
    )

    # Verify prediction works
    predictions = model.predict(X)

    assert len(predictions) == len(y)

    print("Model training and prediction successful.")
