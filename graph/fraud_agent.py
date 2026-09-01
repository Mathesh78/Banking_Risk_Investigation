from langchain_core.messages import SystemMessage

from models.llm import llm

from tools.banking_tools import (
    get_transaction,
    get_fraud_alert,
    get_investigation
)

from tools.case_rag_tools import (
    search_historical_cases
)


FRAUD_TOOLS = [
    get_transaction,
    get_fraud_alert,
    get_investigation,
    search_historical_cases
]


fraud_llm = llm.bind_tools(
    FRAUD_TOOLS
)


FRAUD_PROMPT = """
You are the Fraud and Risk Investigation Agent
in a banking risk investigation system.

Your responsibilities are:

1. Analyze suspicious transactions.
2. Retrieve transaction information.
3. Retrieve fraud alerts.
4. Retrieve investigation information.
5. Search historical investigation cases when
   similar previous cases may help assess the risk.
6. Compare the current transaction with relevant
   historical cases.
7. Provide a grounded risk assessment.

Available tools:

- get_transaction
- get_fraud_alert
- get_investigation
- search_historical_cases

IMPORTANT:

Use MySQL tools to retrieve current banking data.

Use search_historical_cases when you need
historical examples or similar fraud patterns.

Do not invent historical cases.

Do not invent fraud alerts.

Do not invent risk scores.

Do not make a decision based only on historical
cases.

Historical cases are supporting evidence, not proof
that the current transaction is fraudulent.

Use the retrieved information as evidence
for your assessment.

Clearly distinguish:

1. Current transaction facts
2. Fraud indicators
3. Similar historical cases
4. Final risk assessment

Never fabricate information.
"""

def fraud_agent(state):

    print("\n========== FRAUD/RISK AGENT ==========")

    messages = [
        SystemMessage(
            content=FRAUD_PROMPT
        )
    ] + state["messages"]

    response = fraud_llm.invoke(
        messages
    )

    print("Fraud Agent Response:")
    print(response)

    return {
    "messages": [response],
    "fraud_result": response.content
}