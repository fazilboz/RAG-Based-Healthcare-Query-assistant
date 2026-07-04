import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.chains import RetrievalQA

from config import DOCUMENT_FOLDER
from config import VECTOR_DB
from config import GOOGLE_API_KEY

from utils.helper import load_pdf_files

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


def build_vector_database():

    documents = []

    pdfs = load_pdf_files(DOCUMENT_FOLDER)

    for pdf in pdfs:

        loader = PyPDFLoader(pdf)

        documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=500,

        chunk_overlap=100

    )

    chunks = splitter.split_documents(documents)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    db = FAISS.from_documents(
        chunks,
        embeddings
    )

    db.save_local(VECTOR_DB)


def ask_rag(question):

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    db = FAISS.load_local(
        VECTOR_DB,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = db.as_retriever(
        search_kwargs={
            "k":3
        }
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )

    qa = RetrievalQA.from_chain_type(

        llm=llm,

        retriever=retriever,

        return_source_documents=False

    )

    result = qa.invoke(
        {
            "query": question
        }
    )

    return result["result"]