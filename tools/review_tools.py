from database.connection import get_connection


def get_pending_reviews():

    connection = get_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    query = """
        SELECT
            review_id,
            transaction_id,
            risk_level,
            ai_decision,
            ai_confidence,
            reasons,
            review_status,
            created_at
        FROM investigation_reviews
        WHERE review_status = 'WAITING_FOR_HUMAN'
        ORDER BY created_at ASC
    """

    cursor.execute(query)

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results

def complete_review(
    review_id: int,
    human_decision: str,
    human_comments: str
):

    allowed_decisions = {
        "APPROVE",
        "REJECT"
    }

    human_decision = human_decision.upper()

    if human_decision not in allowed_decisions:

        raise ValueError(
            "Human decision must be APPROVE or REJECT"
        )

    connection = get_connection()

    cursor = connection.cursor()

    query = """
        UPDATE investigation_reviews
        SET
            human_decision = %s,
            human_comments = %s,
            review_status = 'COMPLETED',
            reviewed_at = CURRENT_TIMESTAMP
        WHERE review_id = %s
        AND review_status = 'WAITING_FOR_HUMAN'
    """

    cursor.execute(
        query,
        (
            human_decision,
            human_comments,
            review_id
        )
    )

    connection.commit()

    updated_rows = cursor.rowcount

    cursor.close()
    connection.close()

    if updated_rows == 0:

        return {
            "success": False,
            "message": (
                "Review not found or already completed"
            )
        }

    return {
        "success": True,
        "review_id": review_id,
        "human_decision": human_decision,
        "status": "COMPLETED"
    }