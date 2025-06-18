## utils/config.py
import os
from dotenv import load_dotenv

load_dotenv()

def get_env_var(key):
    return os.getenv(key)

---

## README.md
# 🧠 GenAI RAG Product Starter Kit

Build your own GenAI RAG system in under 30 minutes, product-style. Includes vector DB, retrieval, LLM response, guardrails, and Streamlit UI.

## 🔧 Stack
- FAISS (or Pinecone)
- LangChain + OpenAI
- GuardrailsAI
- Streamlit UI
- Replit-ready

## 🛠️ Setup
```bash
git clone https://github.com/yourname/rag-product-starter.git
cd rag-product-starter
pip install -r requirements.txt
cp .env.example .env

# Add files to /data then ingest
data/mydoc.pdf
python ingest/ingest_docs.py

# Run app
streamlit run app/ui.py
```

## 🔁 Customization
- Swap FAISS with Pinecone in `retriever/`
- Adjust Guardrails in `guardrails/`
- Extend with agents in `agents/`
