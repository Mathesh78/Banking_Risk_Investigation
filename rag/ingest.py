from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

from rag.embeddings import embeddings


BASE_DIR = Path(__file__).resolve().parent

DOCUMENTS_DIR = BASE_DIR / "documents" / "policies"

VECTOR_DB_PATH = BASE_DIR / "policy_vector_db"


def load_documents():

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
                    "document_type": "banking_policy"
                }
            )
        )

    return documents


def ingest_policies():

    documents = load_documents()

    print(
        f"Loaded {len(documents)} policy documents"
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(
        documents
    )

    print(
        f"Created {len(chunks)} chunks"
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(
            VECTOR_DB_PATH
        ),
        collection_name="banking_policies"
    )

    print("Policy documents indexed successfully.")

    return vectorstore


if __name__ == "__main__":

    ingest_policies()