import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

DATABASE_PATH = "database/healthcare.db"

VECTOR_DB = "vectorstore/faiss_index"

DOCUMENT_FOLDER = "documents"