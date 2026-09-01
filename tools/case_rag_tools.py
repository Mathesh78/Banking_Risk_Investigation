from langchain_core.tools import tool

from rag.case_retriever import (
    retrieve_historical_cases
)


@tool
def search_historical_cases(
    question: str
) -> str:
    """
    Search historical banking investigation
    cases for similar fraud patterns.
    """

    documents = retrieve_historical_cases(
        question
    )

    if not documents:

        return (
            "No similar historical cases found."
        )

    results = []

    for document in documents:

        source = document.metadata.get(
            "source",
            "unknown"
        )

        results.append(
            f"""
SOURCE: {source}

CASE:
{document.page_content}
"""
        )

    return "\n".join(results)