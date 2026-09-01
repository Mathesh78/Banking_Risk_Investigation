from tools.banking_tools import (
    create_investigation_review
)


def human_review_node(state):

    print("\n========== HUMAN REVIEW ==========")

    risk_decision = state.get(
        "risk_decision",
        {}
    )

    transaction_id = state.get(
        "transaction_id"
    )

    result = create_investigation_review(

        transaction_id=transaction_id,

        risk_level=risk_decision[
            "risk_level"
        ],

        decision=risk_decision[
            "decision"
        ],

        confidence=risk_decision[
            "confidence"
        ],

        reasons=risk_decision[
            "reasons"
        ]
    )

    print("HITL Case Created:")
    print(result)

    return {
        "human_review_required": True,
        "review_id": result["review_id"]
    }