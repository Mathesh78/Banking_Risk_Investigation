from pydantic import BaseModel, Field
from typing import List, Literal


class RiskDecision(BaseModel):

    risk_level: Literal[
        "LOW",
        "MEDIUM",
        "HIGH"
    ] = Field(
        description="Risk level of the transaction"
    )

    decision: Literal[
        "APPROVE",
        "HUMAN_REVIEW"
    ] = Field(
        description="Final recommended decision"
    )

    reasons: List[str] = Field(
        description="Evidence-based reasons for the decision"
    )

    confidence: float = Field(
        description="Confidence score between 0 and 1"
    )