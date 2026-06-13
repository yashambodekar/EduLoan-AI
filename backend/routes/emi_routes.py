from fastapi import APIRouter

from schemas.emi_schema import (
    EMIRequest
)

from services.emi_service import (
    calculate_emi
)

router = APIRouter()

@router.post("/emi")

def emi_calculator(
    data: EMIRequest
):

    result = calculate_emi(
        data.loan_amount,
        data.interest_rate,
        data.tenure_years
    )

    return result