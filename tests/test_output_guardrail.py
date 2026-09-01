from app_guardrails.output_guardrail import validate_evaluation_output


def test_low_risk_approve():

    result = {
        "risk_level": "LOW",
        "decision": "APPROVE",
        "reasons": ["No suspicious indicators"],
        "confidence": 0.9
    }

    valid, message = validate_evaluation_output(result)

    assert valid is True


def test_high_risk_human_review():

    result = {
        "risk_level": "HIGH",
        "decision": "HUMAN_REVIEW",
        "reasons": ["Suspicious transaction"],
        "confidence": 0.95
    }

    valid, message = validate_evaluation_output(result)

    assert valid is True


def test_high_risk_cannot_be_approved():

    result = {
        "risk_level": "HIGH",
        "decision": "APPROVE",
        "reasons": ["Suspicious transaction"],
        "confidence": 0.9
    }

    valid, message = validate_evaluation_output(result)

    assert valid is False


def test_invalid_risk_level():

    result = {
        "risk_level": "CRITICAL",
        "decision": "HUMAN_REVIEW",
        "reasons": ["Risk detected"],
        "confidence": 0.8
    }

    valid, message = validate_evaluation_output(result)

    assert valid is False


def test_invalid_confidence():

    result = {
        "risk_level": "MEDIUM",
        "decision": "HUMAN_REVIEW",
        "reasons": ["Possible risk"],
        "confidence": 1.5
    }

    valid, message = validate_evaluation_output(result)

    assert valid is False