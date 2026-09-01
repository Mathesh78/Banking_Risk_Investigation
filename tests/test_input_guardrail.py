from app_guardrails.input_guardrail import validate_investigation_request


def test_valid_request():

    valid, message = validate_investigation_request(
        "TX1001",
        "Investigate this transaction for fraud risk"
    )

    assert valid is True


def test_invalid_transaction_id():

    valid, message = validate_investigation_request(
        "1001",
        "Investigate this transaction"
    )

    assert valid is False


def test_empty_transaction_id():

    valid, message = validate_investigation_request(
        "",
        "Investigate this transaction"
    )

    assert valid is False


def test_non_banking_question():

    valid, message = validate_investigation_request(
        "TX1001",
        "Tell me a joke"
    )

    assert valid is False