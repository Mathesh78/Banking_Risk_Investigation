import re


def validate_investigation_request(
    transaction_id: str,
    question: str
):

    # ----------------------------------
    # Validate transaction ID
    # ----------------------------------

    if not transaction_id:

        return False, "Transaction ID is required"


    # Example format: TX1001

    if not re.match(
        r"^TX\d+$",
        transaction_id
    ):

        return False, "Invalid transaction ID format"


    # ----------------------------------
    # Validate question
    # ----------------------------------

    if not question:

        return False, "Investigation question is required"


    question_lower = question.lower()


    # ----------------------------------
    # Banking-related keywords
    # ----------------------------------

    banking_keywords = [
        "transaction",
        "fraud",
        "risk",
        "compliance",
        "investigate",
        "payment",
        "transfer",
        "suspicious"
    ]


    is_banking_request = any(
        keyword in question_lower
        for keyword in banking_keywords
    )


    if not is_banking_request:

        return False, (
            "Request is not related "
            "to banking investigation"
        )


    return True, "Request validated"