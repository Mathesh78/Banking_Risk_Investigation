from pathlib import Path

from langchain_chroma import Chroma

from rag.embeddings import embeddings


BASE_DIR = Path(__file__).resolve().parent

VECTOR_DB_PATH = (
    BASE_DIR / "case_vector_db"
)


vectorstore = Chroma(
    persist_directory=str(
        VECTOR_DB_PATH
    ),
    embedding_function=embeddings,
    collection_name="historical_cases"
)


retriever = vectorstore.as_retriever(
    search_kwargs={
        "k": 3
    }
)


def retrieve_historical_cases(
    question: str
):

    return retriever.invoke(
        question
    )