def route_final_decision(state):

    risk_decision = state.get(
        "risk_decision",
        {}
    )

    decision = risk_decision.get(
        "decision"
    )

    print(
        "\n========== FINAL DECISION ROUTER =========="
    )

    print(
        "Decision:",
        decision
    )

    if decision == "APPROVE":

        return "approved"

    return "human_review"