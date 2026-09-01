from langchain_core.messages import HumanMessage

from graph.builder import graph


questions = [
    "Show me the details of transaction TX1001",

    "Why is transaction TX1001 suspicious?",

    "Check whether this transaction follows banking compliance rules"
]


for question in questions:

    print("\n")
    print("=" * 70)
    print("QUESTION:", question)
    print("=" * 70)

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content=question)
            ],
            "next_agent": ""
        }
    )

    print("\nFINAL STATE:")
    print(result)