import math

def calculate_emi(
    loan_amount,
    annual_rate,
    years
):

    monthly_rate = (
        annual_rate / 12 / 100
    )

    months = years * 12

    emi = (
        loan_amount *
        monthly_rate *
        ((1 + monthly_rate) ** months)
    ) / (
        ((1 + monthly_rate) ** months) - 1
    )

    total_payment = emi * months

    interest_paid = (
        total_payment -
        loan_amount
    )

    return {

        "monthly_emi":
        round(emi, 2),

        "total_payment":
        round(total_payment, 2),

        "interest_paid":
        round(interest_paid, 2)
    }