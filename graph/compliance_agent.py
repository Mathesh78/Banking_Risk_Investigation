from langchain_core.messages import SystemMessage

from models.llm import llm

from tools.banking_tools import (
    get_transaction,
    get_customer
)

from tools.rag_tools import (
    search_banking_policy
)


COMPLIANCE_TOOLS = [
    get_transaction,
    get_customer,
    search_banking_policy
]


compliance_llm = llm.bind_tools(
    COMPLIANCE_TOOLS
)


COMPLIANCE_PROMPT = """
You are the Compliance Investigation Agent
in a banking risk investigation system.

Your responsibilities are:

1. Investigate compliance-related questions.
2. Retrieve transaction information when required.
3. Retrieve customer information when required.
4. Search the banking policy knowledge base when
   the question requires a policy or regulatory rule.

Available tools:

- get_transaction
- get_customer
- search_banking_policy

IMPORTANT:

When answering questions about banking policies,
rules, thresholds, procedures, or compliance requirements,
use search_banking_policy.

Do not invent banking policies.

Do not rely on your own knowledge for policy-specific claims.

Use retrieved policy documents as the source of truth.

When possible, mention the policy source used
in your final answer.

Never fabricate information.
"""


def compliance_agent(state):

    print("\n========== COMPLIANCE AGENT ==========")

    messages = [
        SystemMessage(
            content=COMPLIANCE_PROMPT
        )
    ] + state["messages"]

    response = compliance_llm.invoke(
        messages
    )

    print("Compliance Agent Response:")
    print(response)

    return {
    "messages": [response],
    "compliance_result": response.content
}

# def compliance_agent(state):

#     print("\n========== COMPLIANCE AGENT ==========")

#     messages = [
#         SystemMessage(
#             content=COMPLIANCE_PROMPT
#         )
#     ] + state["messages"]

#     print("\n========== DEBUG ==========")

#     print("Total messages:", len(messages))

#     for i, msg in enumerate(messages):

#         content = str(msg.content)

#         print(
#             f"Message {i}: "
#             f"{type(msg).__name__} | "
#             f"{len(content)} characters"
#         )

#     print("===========================\n")

#     response = compliance_llm.invoke(
#         messages
#     )

#     print("Compliance Agent Response:")
#     print(response)

#     return {
#         "messages": [response],
#         "compliance_result": response.content
#     }