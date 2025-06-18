## retriever/faiss_retriever.py
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def load_retriever():
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local("faiss_index", embeddings)
    return db
