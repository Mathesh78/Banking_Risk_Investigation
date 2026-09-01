from langchain_core.tools import tool

from rag.retriever import retrieve_policy


@tool
def search_banking_policy(
    question: str
) -> str:
    """
    Search the banking policy knowledge base
    for relevant compliance policies.
    """

    documents = retrieve_policy(
        question
    )

    if not documents:

        return "No relevant banking policy found."

    results = []

    for document in documents:

        results.append(
            f"""
SOURCE: {document.metadata.get("source")}

CONTENT:
{document.page_content}
"""
        )

    return "\n".join(results)