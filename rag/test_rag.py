from rag.retriever import retrieve_policy


question = """
What should happen when an international
transaction is above INR 50,000?
"""


documents = retrieve_policy(question)


print("\n========== RAG RESULTS ==========\n")


for document in documents:

    print("SOURCE:")
    print(document.metadata)

    print("\nCONTENT:")
    print(document.page_content)

    print("\n" + "=" * 60)