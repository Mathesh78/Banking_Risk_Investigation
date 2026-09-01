from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

from rag.embeddings import embeddings


BASE_DIR = Path(__file__).resolve().parent

DOCUMENTS_DIR = (
    BASE_DIR
    / "documents"
    / "historical_cases"
)

VECTOR_DB_PATH = (
    BASE_DIR
    / "case_vector_db"
)


def load_cases():

    documents = []

    for file_path in DOCUMENTS_DIR.glob("*.txt"):

        text = file_path.read_text(
            encoding="utf-8"
        )

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": file_path.name,
                    "document_type": "historical_case"
                }
            )
        )

    return documents


def ingest_cases():

    documents = load_cases()

    print(
        f"Loaded {len(documents)} historical cases"
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(
        documents
    )

    print(
        f"Created {len(chunks)} case chunks"
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(
            VECTOR_DB_PATH
        ),
        collection_name="historical_cases"
    )

    print(
        "Historical cases indexed successfully."
    )

    return vectorstore


if __name__ == "__main__":
    ingest_cases()