from langchain_core.messages import SystemMessage

from models.llm import llm
from models.schemas import RiskDecision

from app_guardrails.output_guardrail import (
    validate_evaluation_output
)


EVALUATOR_PROMPT = """
You are the Risk Evaluator Agent in a banking
risk investigation system.

You receive a consolidated investigation summary.

Your responsibility is to determine:

1. Risk level
2. Recommended decision
3. Reasons
4. Confidence

==================================================
ALLOWED VALUES
==================================================

risk_level MUST be exactly one of:

LOW
MEDIUM
HIGH

decision MUST be exactly one of:

APPROVE
HUMAN_REVIEW

==================================================
DECISION RULES
==================================================

- LOW risk may be APPROVE.
- MEDIUM risk should normally be HUMAN_REVIEW.
- HIGH risk MUST be HUMAN_REVIEW.
- NEVER approve HIGH risk.
- NEVER invent evidence.
- Base your decision ONLY on the investigation evidence.

==================================================
IMPORTANT
==================================================

You MUST provide ALL four fields:

risk_level
decision
reasons
confidence

risk_level is REQUIRED.

Never omit risk_level.

If the investigation evidence is insufficient
to determine the risk reliably, use:

risk_level = HIGH
decision = HUMAN_REVIEW

and explain the missing evidence in reasons.

Return the required structured output.
"""


def evaluator_agent(state):

    print("\n========== EVALUATOR AGENT ==========")

    investigation = state.get(
        "investigation_summary",
        "No investigation summary available."
    )

    prompt = f"""
Investigation Summary:

{investigation}

Evaluate this investigation and produce
the final risk recommendation.
"""

    messages = [
        SystemMessage(
            content=EVALUATOR_PROMPT
        ),
        {
            "role": "user",
            "content": prompt
        }
    ]

    # ==========================================
    # Structured LLM
    # ==========================================

    structured_llm = llm.with_structured_output(
        RiskDecision
    )

    response = structured_llm.invoke(
        messages
    )

    # ==========================================
    # Convert Pydantic object → dictionary
    # ==========================================

    result = response.model_dump()

    print("\nEvaluator Result:")
    print(result)

    # ==========================================
    # OUTPUT GUARDRAIL
    # ==========================================

    valid, message = validate_evaluation_output(
        result
    )

    print("\nOutput Guardrail:")
    print(message)

    # ==========================================
    # Invalid output
    # ==========================================

    if not valid:

        return {
            "risk_decision": {
                "risk_level": "HIGH",
                "decision": "HUMAN_REVIEW",
                "reasons": [
                    message
                ],
                "confidence": 0.0
            }
        }

    # ==========================================
    # Valid output
    # ==========================================

    return {
        "risk_decision": result
    }