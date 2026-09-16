
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load trained model
model = joblib.load("/content/ADS/best_model.pkl")

app = FastAPI(
    title="Revenue Prediction API",
    description="FastAPI service for predicting revenue using the trained model",
    version="1.0"
)


class PredictionInput(BaseModel):
    product: str
    quantity: float
    unit_price: float
    region: str
    year: int
    month: int
    day: int
    weekday: str
    time_of_day: str
    product_category: str


@app.get("/")
def home():
    return {"message": "Revenue Prediction API is running"}


@app.post("/predict")
def predict(data: PredictionInput):

    input_data = pd.DataFrame([data.model_dump()])

    prediction = model.predict(input_data)

    return {
        "predicted_revenue": float(prediction[0])
    }
