from pathlib import Path

from langchain_chroma import Chroma

from rag.embeddings import embeddings


BASE_DIR = Path(__file__).resolve().parent

CASE_VECTOR_DB_PATH = BASE_DIR / "case_vector_db"


case_vectorstore = Chroma(
    persist_directory=str(CASE_VECTOR_DB_PATH),
    embedding_function=embeddings,
    collection_name="historical_cases"
)