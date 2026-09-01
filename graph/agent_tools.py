from langgraph.prebuilt import ToolNode
from tools.rag_tools import (
    search_banking_policy
)

from tools.case_rag_tools import (
    search_historical_cases
)

from tools.banking_tools import (
    get_customer,
    get_account,
    get_transaction,
    get_fraud_alert,
    get_investigation
)


TRANSACTION_TOOLS = [
    get_customer,
    get_account,
    get_transaction
]


FRAUD_TOOLS = [
    get_transaction,
    get_fraud_alert,
    get_investigation,
    search_historical_cases
]

COMPLIANCE_TOOLS = [
    get_transaction,
    get_customer,
    search_banking_policy
]


transaction_tool_node = ToolNode(  #ToolNode is a LangGraph component that executes the tools requested by the LLM.
    TRANSACTION_TOOLS
)


fraud_tool_node = ToolNode(
    FRAUD_TOOLS
)


compliance_tool_node = ToolNode(
    COMPLIANCE_TOOLS
)