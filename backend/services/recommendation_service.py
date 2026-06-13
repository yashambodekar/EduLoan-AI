import json

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

with open(
    BASE_DIR / "data" / "lenders.json",
    "r"
) as f:

    lenders = json.load(f)


def recommend_lenders(
    probability
):

    if probability >= 80:

        return lenders[:3]

    elif probability >= 60:

        return lenders[1:4]

    else:

        return [
            {
                "name":
                "Profile Improvement Needed",

                "interest_rate":
                "N/A",

                "max_amount":
                "N/A",

                "risk":
                "High"
            }
        ]