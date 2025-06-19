## retriever/faiss_retriever.py
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

import utils.config 
from utils.config import get_env_var
openai_key = get_env_var("OPENAI_API_KEY")

def load_retriever():
    embeddings = OpenAIEmbeddings(openai_key = openai_key)
    db = FAISS.load_local("faiss_index", embeddings)
    return db
