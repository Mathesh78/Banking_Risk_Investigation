ALLOWED_RISK_LEVELS = {
    "LOW",
    "MEDIUM",
    "HIGH"
}

ALLOWED_DECISIONS = {
    "APPROVE",
    "HUMAN_REVIEW"
}


def validate_evaluation_output(result):

    if not result:
        return False, "Evaluator returned empty output"

    required_fields = [
        "risk_level",
        "decision",
        "reasons",
        "confidence"
    ]

    for field in required_fields:
        if field not in result:
            return False, f"Missing required field: {field}"

    risk_level = result["risk_level"]
    decision = result["decision"]
    confidence = result["confidence"]

    if risk_level not in ALLOWED_RISK_LEVELS:
        return False, f"Invalid risk level: {risk_level}"

    if decision not in ALLOWED_DECISIONS:
        return False, f"Invalid decision: {decision}"

    if not isinstance(confidence, (int, float)):
        return False, "Confidence must be numeric"

    if not 0 <= confidence <= 1:
        return False, "Confidence must be between 0 and 1"

    if risk_level == "HIGH" and decision == "APPROVE":
        return False, "HIGH risk transactions cannot be automatically approved"

    return True, "Output validated"