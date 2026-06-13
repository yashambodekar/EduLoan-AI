import joblib
import pandas as pd

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(
    BASE_DIR / "models" / "loan_model.pkl"
)

scaler = joblib.load(
    BASE_DIR / "models" / "scaler.pkl"
)


def predict_loan(features):

    df = pd.DataFrame([features])

    scaled = scaler.transform(df)

    probability = (
        model.predict_proba(scaled)[0][1]
    )

    prediction = (
        model.predict(scaled)[0]
    )

    return {

        "approval_probability":
        round(probability * 100, 2),

        "prediction":
        "Approved"
        if prediction == 1
        else "Rejected",

        "scaled_input":
        scaled
    }