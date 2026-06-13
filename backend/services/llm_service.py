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
    negative_factors
):

  prompt = f"""
  You are an AI Education Loan Advisor.

  Prediction: {prediction}
  Approval Probability: {probability}%

  Top Positive Factors:
  {positive_factors}

  Top Negative Factors:
  {negative_factors}

  Generate:

  1. Approval Summary (2 lines)
  2. Key Strengths (bullet points)
  3. Potential Concerns (bullet points)
  4. Recommendation to improve approval chances

  Keep the response professional and student-friendly.
  """

  response = llm.invoke(
        prompt
    )

  return response.content