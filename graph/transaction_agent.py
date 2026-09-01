from langchain_core.messages import SystemMessage

from models.llm import llm

from tools.banking_tools import (
    get_customer,
    get_account,
    get_transaction
)


TRANSACTION_TOOLS = [
    get_customer,
    get_account,
    get_transaction
]


transaction_llm = llm.bind_tools(
    TRANSACTION_TOOLS
)


TRANSACTION_PROMPT = """
You are the Transaction Investigation Agent
in a banking risk investigation system.

Your responsibilities are:

- Retrieve transaction information.
- Retrieve customer information.
- Retrieve account information.
- Explain transaction details.
- Never perform fraud analysis.
- Never perform compliance analysis.

Available tools:

get_customer
get_account
get_transaction

Use MySQL data returned by these tools as the source of truth.

Never invent information.

Use only the tools provided to you.

Once you have enough information, provide
a concise transaction analysis.
"""


def transaction_agent(state):

    print("\n========== TRANSACTION AGENT ==========")

    messages = [
        SystemMessage(
            content=TRANSACTION_PROMPT
        )
    ] + state["messages"]

    response = transaction_llm.invoke(
        messages
    )

    print("Transaction Agent Response:")
    print(response)

    return {
    "messages": [response],
    "transaction_result": response.content
}