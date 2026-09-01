# from langchain_core.messages import HumanMessage

# from graph.builder import graph


# result = graph.invoke(
#     {
#         "messages": [
#             HumanMessage(
#                 content="Check transaction TX1001"
#             )
#         ]
#     }
# )


# print("\n==============================")
# print("FINAL RESULT")
# print("==============================")

# for message in result["messages"]:
#     print("\n", message)

# from langchain_core.messages import HumanMessage

# from graph.builder import graph


# result = graph.invoke(
#     {
#         "messages": [
#             HumanMessage(
#                 content="Check whether TX1001 violates our international transfer policy."
#             )
#         ],
#         "next_agent": ""
#     }
# )


# print("\n")
# print("=" * 70)
# print("FINAL RESULT")
# print("=" * 70)

# for message in result["messages"]:
#     print("\n", message)

from langchain_core.messages import HumanMessage
from graph.builder import graph

result = graph.invoke(
    {
        "transaction_id": "TX1001",  # <-- ADD THIS KEY HERE
        "messages": [
            HumanMessage(
                content="Check whether TX1001 violates our international transfer policy."
            )
        ],
        "next_agent": ""
    }
)

print("\n")
print("=" * 70)
print("FINAL RESULT")
print("=" * 70)

for message in result["messages"]:
    print("\n", message)