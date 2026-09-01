from typing import Annotated

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

from typing_extensions import TypedDict


class State(TypedDict, total=False):

    messages: Annotated[
        list[BaseMessage],
        add_messages
    ]

    next_agent: str

    transaction_id: str

    transaction_result: str

    fraud_result: str

    compliance_result: str

    investigation_summary: str

    risk_decision: dict

    human_review_required: bool
    
    review_id: int
    
    human_decision: str
    
    human_comments: str