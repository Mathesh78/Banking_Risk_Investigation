from langchain_core.messages import SystemMessage

from models.llm import llm


SUPERVISOR_PROMPT = """
You are the Supervisor Agent for a Banking Risk Investigation System.

Your job is to decide which specialist should handle the user's request.

Available specialists:

1. transaction_agent
   - Handles transaction information
   - Customer account information
   - Transaction history

2. fraud_agent
   - Handles fraud detection
   - Risk analysis
   - Suspicious transaction investigation

3. compliance_agent
   - Handles banking policies
   - Regulatory requirements
   - Compliance checks

Choose the most appropriate specialist.

Return ONLY one of:

transaction_agent
fraud_agent
compliance_agent
"""


def supervisor_agent(state):

    print("\n========== SUPERVISOR ==========")

    question = state["messages"][-1].content

    response = llm.invoke([
        SystemMessage(content=SUPERVISOR_PROMPT),
        {
            "role": "user",
            "content": question
        }
    ])

    decision = response.content.strip().lower()

    print("Supervisor decision:", decision)

    if "fraud" in decision:
        next_agent = "fraud_agent"

    elif "compliance" in decision:
        next_agent = "compliance_agent"

    else:
        next_agent = "transaction_agent"

    return {
        "next_agent": next_agent
    }