import shap
import joblib
import pandas as pd

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

background_data = joblib.load(
    BASE_DIR / "models" / "background_data.pkl"
)

model = joblib.load(
    BASE_DIR / "models" / "loan_model.pkl"
)

explainer = shap.LinearExplainer(
    model,
    background_data
)

def explain_prediction(
    scaled_input,
    feature_names
):

    shap_values = explainer.shap_values(
        scaled_input
    )

    print(shap_values)

    df = pd.DataFrame({
        "feature": feature_names,
        "impact": shap_values[0]
    })

    print(df.columns)
    print(df)

    positive = (
        df.sort_values(
            "impact",
            ascending=False
        )
        .head(3)
    )

    negative = (
        df.sort_values(
            "impact"
        )
        .head(3)
    )

    return {
        "top_positive_factors":
        positive.to_dict(
            orient="records"
        ),

        "top_negative_factors":
        negative.to_dict(
            orient="records"
        )
    }