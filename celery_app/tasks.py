from celery_app.celery_config import celery
from graph.builder import graph


@celery.task
def investigate_transaction(transaction_id, question):

    result = graph.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ],
            "original_question": question,
            "transaction_id": transaction_id,
        }
    )

    return {
        "transaction_id": transaction_id,
        "investigation_summary": result.get(
            "investigation_summary"
        ),
        "risk_decision": result.get(
            "risk_decision"
        ),
        "human_review_required": result.get(
            "human_review_required",
            False
        ),
        "review_id": result.get(
            "review_id"
        )
    }