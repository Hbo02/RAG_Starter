## retriever/faiss_retriever.py
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from ingest.ingest_docs import ingest
import utils.config 
from utils.config import get_env_var
openai_api_key = get_env_var("OPENAI_API_KEY")

def load_retriever():
    if not os.path.exists("faiss_index"):
        print("FAISS index not found. Running ingestion...")
        ingest()
    embeddings = OpenAIEmbeddings(openai_api_key = openai_api_key)
    db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    return db
