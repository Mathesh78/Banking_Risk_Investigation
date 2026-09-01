# api/main.py


from app_guardrails.input_guardrail import (
    validate_investigation_request
)

from tools.review_tools import complete_review

from fastapi import FastAPI, HTTPException

from celery_app.tasks import investigate_transaction

from celery.result import AsyncResult

from celery_app.celery_config import celery

from api.schemas import InvestigationRequest

from graph.builder import graph

from graph.state import State

from graph.ReviewRequest import ReviewRequest

app = FastAPI(
    title="Banking Risk Investigation API",
    version="1.0.0"
)


@app.get("/")
def root():

    return {
        "message": "Banking Risk Investigation API"
    }

@app.post("/investigate")
def investigate(
    request: InvestigationRequest
):

    # ----------------------------------
    # Input Guardrail
    # ----------------------------------

    valid, message = validate_investigation_request(
        request.transaction_id,
        request.question
    )


    if not valid:

        raise HTTPException(
            status_code=400,
            detail=message
        )


    # ----------------------------------
    # Submit Celery task
    # ----------------------------------

    task = investigate_transaction.delay(
        request.transaction_id,
        request.question
    )


    return {
        "transaction_id": request.transaction_id,
        "task_id": task.id,
        "status": "queued"
    }

@app.get("/task/{task_id}")
def get_task(task_id: str):

    task = AsyncResult(   #creates an object that lets your FastAPI endpoint track that background task.
        task_id,
        app=celery
    )

    if task.state == "SUCCESS":

        return {
            "task_id": task_id,
            "status": "completed",
            "response": task.result
        }

    elif task.state == "FAILURE":

        return {
            "task_id": task_id,
            "status": "failed"
        }

    return {
        "task_id": task_id,
        "status": task.state.lower()
    }

from tools.review_tools import (
    get_pending_reviews
)


@app.get("/reviews/pending")
def pending_reviews():

    reviews = get_pending_reviews()

    return {
        "reviews": reviews
    }

@app.post("/reviews/{review_id}")
def complete_human_review(
    review_id: int,
    request: ReviewRequest
):

    try:

        result = complete_review(
            review_id=review_id,
            human_decision=request.human_decision,
            human_comments=request.human_comments
        )

        return result

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )