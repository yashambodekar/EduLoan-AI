from fastapi import APIRouter

from schemas.loan_schema import LoanRequest

from services.feature_engineering import (
    create_features
)

from services.prediction_service import (
    predict_loan
)

from services.shap_service import (
    explain_prediction
)

from services.llm_service import (
    generate_explanation
)

router = APIRouter()

@router.post("/predict")

def predict(
    data: LoanRequest
):

    features = create_features(
        data.dict()
    )

    result = predict_loan(
        features
    )

    explanation = explain_prediction(

        result["scaled_input"],

        list(features.keys())
    )

    positive = explanation[
    "top_positive_factors"
    ]

    negative = explanation[
    "top_negative_factors"
    ]

    llm_explanation = generate_explanation(
    result["prediction"],
    result["approval_probability"],
    positive,
    negative
    )

    return {

    "approval_probability":
    result["approval_probability"],

    "prediction":
    result["prediction"],

    "top_positive_factors":
    positive,

    "top_negative_factors":
    negative,

    "llm_explanation":
    llm_explanation
}