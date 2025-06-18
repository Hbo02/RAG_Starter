## ingest/ingest_docs.py
import os
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

def ingest():
    if not os.path.exists("data"):
        raise FileNotFoundError("📁 'data/' folder not found. Please add your documents.")

    print("📥 Loading documents from /data...")
    loader = DirectoryLoader("data")
    documents = loader.load()

    print(f"📄 Loaded {len(documents)} documents. Splitting into chunks...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    print(f"🧠 Creating embeddings for {len(docs)} chunks...")
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)

    print("💾 Saving FAISS index to /faiss_index...")
    db.save_local("faiss_index")
    print("✅ Ingest complete!")

if __name__ == "__main__":
    ingest()


