# api/schemas.py

from pydantic import BaseModel


class InvestigationRequest(BaseModel):

    transaction_id: str

    question: str