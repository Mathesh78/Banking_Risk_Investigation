from rag.case_retriever import (
    retrieve_historical_cases
)


question = """
Find historical fraud cases involving
large international transfers and unusual
customer transaction behavior.
"""


documents = retrieve_historical_cases(
    question
)


print(
    "\n========== HISTORICAL CASE RESULTS ==========\n"
)


for document in documents:

    print(
        "SOURCE:",
        document.metadata
    )

    print(
        "\nCONTENT:"
    )

    print(
        document.page_content
    )

    print(
        "\n" + "=" * 60
    )