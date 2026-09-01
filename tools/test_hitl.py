from tools.banking_tools import (
    create_investigation_review
)


result = create_investigation_review(

    transaction_id="TX1001",

    risk_level="HIGH",

    decision="HUMAN_REVIEW",

    confidence=0.94,

    reasons=[
        "High transaction amount",
        "International transaction",
        "Fraud alert detected"
    ]
)


print("\n========== HITL REVIEW ==========")

print(result)