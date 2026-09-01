from langchain_core.messages import SystemMessage

from models.llm import llm


INVESTIGATOR_PROMPT = """
You are the Investigator Agent in a banking
risk investigation system.

Your responsibility is to consolidate evidence
collected by specialist agents.

You will receive:

1. Transaction analysis
2. Fraud/Risk analysis
3. Compliance analysis

Your job is to:

- Compare the evidence.
- Identify common risk indicators.
- Identify conflicting evidence.
- Produce a structured investigation summary.
- Do not invent facts.
- Do not make unsupported claims.
- Do not make the final approval/rejection decision.

The Evaluator Agent will make the final risk decision.

Clearly separate:

- Transaction facts
- Fraud indicators
- Compliance findings
- Overall investigation summary
"""


def investigator_agent(state):

    print("\n========== INVESTIGATOR AGENT ==========")

    transaction_result = state.get(
        "transaction_result",
        "No transaction analysis available."
    )

    fraud_result = state.get(
        "fraud_result",
        "No fraud analysis available."
    )

    compliance_result = state.get(
        "compliance_result",
        "No compliance analysis available."
    )

    prompt = f"""
Transaction Analysis:

{transaction_result}


Fraud/Risk Analysis:

{fraud_result}


Compliance Analysis:

{compliance_result}


Based on the above evidence, create
a consolidated investigation summary.
"""

    messages = [
        SystemMessage(
            content=INVESTIGATOR_PROMPT
        ),
        {
            "role": "user",
            "content": prompt
        }
    ]

    response = llm.invoke(messages)

    print("Investigator Result:")
    print(response.content)

    return {
        "messages": [response],
        "investigation_summary": response.content
    }