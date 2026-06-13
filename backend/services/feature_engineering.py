import pandas as pd

def create_features(data):

    total_income = (
        data["ApplicantIncome"]
        +
        data["CoapplicantIncome"]
    )

    loan_income_ratio = (
        data["LoanAmount"]
        /
        (total_income + 1)
    )

    emi_burden = (
        data["LoanAmount"]
        /
        data["Loan_Amount_Term"]
    )

    income_per_dependent = (
        total_income
        /
        (data["Dependents"] + 1)
    )

    return {
        **data,

        "TotalIncome":
        total_income,

        "LoanIncomeRatio":
        loan_income_ratio,

        "EMI_Burden":
        emi_burden,

        "IncomePerDependent":
        income_per_dependent
    }