from langgraph.graph import (
    StateGraph,
    START,
    END
)

from graph.hitl import human_review_node

from graph.decision_router import (
    route_final_decision
)

from langgraph.prebuilt import tools_condition

from graph.state import State

from graph.supervisor import supervisor_agent

from graph.transaction_agent import transaction_agent
from graph.fraud_agent import fraud_agent
from graph.compliance_agent import compliance_agent

from graph.investigator_agent import investigator_agent
from graph.evaluator_agent import evaluator_agent

from graph.agent_tools import (
    transaction_tool_node,
    fraud_tool_node,
    compliance_tool_node
)

from graph.router import route_to_agent


# =====================================================
# CREATE GRAPH
# =====================================================

builder = StateGraph(State)


# =====================================================
# AGENTS
# =====================================================

builder.add_node(
    "supervisor",
    supervisor_agent
)

builder.add_node(
    "transaction_agent",
    transaction_agent
)

builder.add_node(
    "fraud_agent",
    fraud_agent
)

builder.add_node(
    "compliance_agent",
    compliance_agent
)

builder.add_node(
    "investigator",
    investigator_agent
)

builder.add_node(
    "evaluator",
    evaluator_agent
)

builder.add_node(
    "human_review",
    human_review_node
)

# =====================================================
# TOOL NODES
# =====================================================

builder.add_node(
    "transaction_tools",
    transaction_tool_node
)

builder.add_node(
    "fraud_tools",
    fraud_tool_node
)

builder.add_node(
    "compliance_tools",
    compliance_tool_node
)


# =====================================================
# START
# =====================================================

builder.add_edge(
    START,
    "supervisor"
)


# =====================================================
# SUPERVISOR ROUTING
# =====================================================

builder.add_conditional_edges(
    "supervisor",
    route_to_agent,
    {
        "transaction_agent": "transaction_agent",
        "fraud_agent": "fraud_agent",
        "compliance_agent": "compliance_agent",
        "__end__": END
    }
)


# =====================================================
# TRANSACTION AGENT
# =====================================================

builder.add_conditional_edges(
    "transaction_agent",
    tools_condition,
    {
        "tools": "transaction_tools",
        "__end__": "investigator"
    }
)

builder.add_edge(
    "transaction_tools",
    "transaction_agent"
)


# =====================================================
# FRAUD AGENT
# =====================================================

builder.add_conditional_edges(
    "fraud_agent",
    tools_condition,
    {
        "tools": "fraud_tools",
        "__end__": "investigator"
    }
)

builder.add_edge(
    "fraud_tools",
    "fraud_agent"
)


# =====================================================
# COMPLIANCE AGENT
# =====================================================

builder.add_conditional_edges(
    "compliance_agent",
    tools_condition,
    {
        "tools": "compliance_tools",
        "__end__": "investigator"
    }
)

builder.add_edge(
    "compliance_tools",
    "compliance_agent"
)


# =====================================================
# INVESTIGATOR
# =====================================================

builder.add_edge(
    "investigator",
    "evaluator"
)

builder.add_conditional_edges(
    "evaluator",
    route_final_decision,
    {
        "approved": END,
        "human_review": "human_review"
    }
)
# =====================================================
# EVALUATOR
# =====================================================

builder.add_edge(
    "human_review",
    END
)

# builder.add_edge(
#     "evaluator",
#     END
# )


# =====================================================
# COMPILE
# =====================================================

graph = builder.compile()