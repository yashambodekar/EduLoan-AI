from fastapi import FastAPI
from pydantic import BaseModel

import joblib
import pandas as pd

app = FastAPI()

model = joblib.load(
    "../models/loan_model.pkl"
)

scaler = joblib.load(
    "../models/scaler.pkl"
)


class LoanRequest(BaseModel):

    Gender: int
    Married: int
    Dependents: int
    Education: int
    Self_Employed: int
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: int


@app.get("/")
def home():
    return {
        "message":
        "EduLoan AI API Running"
    }


@app.post("/predict")
def predict(data: LoanRequest):

    total_income = (
        data.ApplicantIncome +
        data.CoapplicantIncome
    )

    loan_income_ratio = (
        data.LoanAmount /
        (total_income + 1)
    )

    emi_burden = (
        data.LoanAmount /
        data.Loan_Amount_Term
    )

    income_per_dependent = (
        total_income /
        (data.Dependents + 1)
    )

    input_df = pd.DataFrame([{

        "Gender":
        data.Gender,

        "Married":
        data.Married,

        "Dependents":
        data.Dependents,

        "Education":
        data.Education,

        "Self_Employed":
        data.Self_Employed,

        "ApplicantIncome":
        data.ApplicantIncome,

        "CoapplicantIncome":
        data.CoapplicantIncome,

        "LoanAmount":
        data.LoanAmount,

        "Loan_Amount_Term":
        data.Loan_Amount_Term,

        "Credit_History":
        data.Credit_History,

        "Property_Area":
        data.Property_Area,

        "TotalIncome":
        total_income,

        "LoanIncomeRatio":
        loan_income_ratio,

        "EMI_Burden":
        emi_burden,

        "IncomePerDependent":
        income_per_dependent
    }])

    input_scaled = scaler.transform(
        input_df
    )

    probability = (
        model.predict_proba(
            input_scaled
        )[0][1]
    )

    prediction = (
        model.predict(
            input_scaled
        )[0]
    )

    return {

        "approval_probability":
        round(probability * 100, 2),

        "prediction":
        "Approved"
        if prediction == 1
        else "Rejected"
    }