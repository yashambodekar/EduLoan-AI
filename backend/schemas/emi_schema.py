from pydantic import BaseModel

class EMIRequest(BaseModel):

    loan_amount: float

    interest_rate: float

    tenure_years: int