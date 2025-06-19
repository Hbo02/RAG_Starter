## ingest/ingest_docs.py
import os
from langchain.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

import utils.config 
from utils.config import get_env_var
openai_api_key=get_env_var("OPENAI_API_KEY")

#from dotenv import load_dotenv
#load_dotenv()

SUPPORTED_EXTENSIONS = [".pdf", ".txt", ".md"]

def load_documents(data_dir="data"):
    if not os.path.exists(data_dir):
        raise FileNotFoundError("❌ 'data/' directory not found. Please add it and upload your files.")

    documents = []
    for filename in os.listdir(data_dir):
        filepath = os.path.join(data_dir, filename)
        ext = os.path.splitext(filename)[-1].lower()

        try:
            if ext == ".pdf":
                loader = PyPDFLoader(filepath)
            elif ext in [".txt", ".md"]:
                loader = TextLoader(filepath)
            else:
                print(f"⚠️ Skipping unsupported file type: {filename}")
                continue

            docs = loader.load()
            documents.extend(docs)
            print(f"✅ Loaded: {filename}")

        except Exception as e:
            print(f"❌ Error loading {filename}: {str(e)}")

    if not documents:
        raise ValueError("No valid documents loaded. Check file types or contents.")
    return documents

def ingest():
    print("📥 Starting ingestion process...")
    raw_docs = load_documents()

    print(f"✂️ Splitting {len(raw_docs)} documents into chunks...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(raw_docs)

    print(f"🧠 Creating embeddings for {len(docs)} chunks...")
    embeddings = OpenAIEmbeddings(openai_api_key = openai_api_key)
    db = FAISS.from_documents(docs, embeddings)

    print("💾 Saving FAISS index to 'faiss_index/'")
    db.save_local("faiss_index")

    print("✅ Done! You can now query your RAG system.")

if __name__ == "__main__":
    ingest()


