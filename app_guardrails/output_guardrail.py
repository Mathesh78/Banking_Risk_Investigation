ALLOWED_RISK_LEVELS = {
    "LOW",
    "MEDIUM",
    "HIGH"
}

ALLOWED_DECISIONS = {
    "APPROVE",
    "HUMAN_REVIEW",
    "REJECT"
}


def validate_evaluation_output(result):

    # --------------------------------
    # Check result exists
    # --------------------------------

    if not result:

        return False, "Evaluator returned empty output"


    # --------------------------------
    # Check required fields
    # --------------------------------

    required_fields = [
        "risk_level",
        "decision",
        "confidence"
    ]

    for field in required_fields:

        if field not in result:

            return False, (
                f"Missing required field: {field}"
            )


    # --------------------------------
    # Validate risk level
    # --------------------------------

    risk_level = result["risk_level"]

    if risk_level not in ALLOWED_RISK_LEVELS:

        return False, (
            f"Invalid risk level: {risk_level}"
        )


    # --------------------------------
    # Validate decision
    # --------------------------------

    decision = result["decision"]

    if decision not in ALLOWED_DECISIONS:

        return False, (
            f"Invalid decision: {decision}"
        )


    # --------------------------------
    # Validate confidence
    # --------------------------------

    confidence = result["confidence"]

    if not isinstance(
        confidence,
        (int, float)
    ):

        return False, (
            "Confidence must be a number"
        )


    if not 0 <= confidence <= 1:

        return False, (
            "Confidence must be between 0 and 1"
        )


    return True, "Output validated"