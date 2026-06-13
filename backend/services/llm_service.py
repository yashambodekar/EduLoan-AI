# services/llm_service.py

import os

from dotenv import load_dotenv

from langchain_google_genai import (
    ChatGoogleGenerativeAI
)

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3,
    google_api_key=os.getenv(
        "GOOGLE_API_KEY"
    )
)


def generate_explanation(
    prediction,
    probability,
    positive_factors,
    negative_factors,
    recommended_lenders
):

  prompt = f"""
You are an AI Education Loan Advisor.

Prediction:
{prediction}

Approval Probability:
{probability}%

Positive Factors:
{positive_factors}

Negative Factors:
{negative_factors}

Recommended Lenders:
{recommended_lenders}

Generate:

1. Approval Summary
2. Key Strengths
3. Concerns
4. Why these lenders are recommended

Keep response concise.
"""

  response = llm.invoke(
        prompt
    )

  return response.content