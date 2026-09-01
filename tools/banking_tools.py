from pathlib import Path

from langchain_core.tools import tool

from database.connection import get_connection


QUERY_FOLDER = (
    Path(__file__).parent.parent
    / "database"
    / "queries"
)


@tool
def get_transaction(transaction_id: str):
    """
    Get transaction details using transaction ID.
    """

    query_file = QUERY_FOLDER / "transaction_queries.sql"

    query = query_file.read_text()

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    try:

        cursor.execute(query, (transaction_id,))

        result = cursor.fetchone()

        if result is None:
            return f"No transaction found for {transaction_id}"

        return result

    finally:

        cursor.close()
        connection.close()

@tool
def get_customer(customer_id: str):
    """
    Get customer details using customer ID.
    """

    query_file = QUERY_FOLDER / "customer_queries.sql"

    query = query_file.read_text()

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:

        cursor.execute(query, (customer_id,))

        result = cursor.fetchone()

        if result is None:
            return f"No customer found for {customer_id}"

        return result

    finally:

        cursor.close()
        connection.close()

@tool
def get_account(account_id: str):
    """
    Get account details using account ID.
    """

    query_file = QUERY_FOLDER / "account_queries.sql"

    query = query_file.read_text()

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:

        cursor.execute(query, (account_id,))

        result = cursor.fetchone()

        if result is None:
            return f"No account found for {account_id}"

        return result

    finally:

        cursor.close()
        connection.close()

@tool
def get_fraud_alert(transaction_id: str):
    """
    Get fraud and risk information for a transaction.
    """

    query_file = QUERY_FOLDER / "fraud_queries.sql"

    query = query_file.read_text()

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:

        cursor.execute(query, (transaction_id,))

        result = cursor.fetchone()

        if result is None:
            return f"No fraud alert found for transaction {transaction_id}"

        return result

    finally:

        cursor.close()
        connection.close()

@tool
def get_investigation(transaction_id: str):
    """
    Get investigation details for a transaction.
    """

    query_file = QUERY_FOLDER / "investigation_queries.sql"

    query = query_file.read_text()

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:

        cursor.execute(query, (transaction_id,))

        result = cursor.fetchone()

        if result is None:
            return f"No investigation found for transaction {transaction_id}"

        return result

    finally:

        cursor.close()
        connection.close()


TRANSACTION_TOOLS = [
    get_customer,
    get_account,
    get_transaction
]


FRAUD_TOOLS = [
    get_transaction,
    get_fraud_alert,
    get_investigation
]


COMPLIANCE_TOOLS = [
    get_transaction,
    get_customer
]


import json

from database.connection import get_connection


def create_investigation_review(
    transaction_id: str,
    risk_level: str,
    decision: str,
    confidence: float,
    reasons: list
):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
        INSERT INTO investigation_reviews
        (
            transaction_id,
            risk_level,
            ai_decision,
            ai_confidence,
            reasons,
            review_status
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s,
            'WAITING_FOR_HUMAN'
        )
    """

    cursor.execute(
        query,
        (
            transaction_id,
            risk_level,
            decision,
            confidence,
            json.dumps(reasons)
        )
    )

    connection.commit()

    review_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return {
        "review_id": review_id,
        "transaction_id": transaction_id,
        "status": "WAITING_FOR_HUMAN"
    }
