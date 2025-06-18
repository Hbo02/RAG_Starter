# 🧠 GenAI RAG Product Starter Kit

A product-first, hands-on starter kit to build and test your own Retrieval-Augmented Generation (RAG) app, complete with safety checks, evaluation, and real user experience—all in under an hour.

## 🌟 What You’ll Learn & Build
- Upload your own documents
- Build a working RAG pipeline (retriever + LLM)
- Add safety checks with Guardrails
- Run evaluations on real queries
- Deploy to Replit in 1-click
- Plug into Flowise (optional)

## 🔧 Tech Stack
| Feature         | Tool |
|----------------|------|
| Retrieval       | FAISS (local) or Pinecone |
| LLM             | OpenAI via LangChain |
| UI              | Streamlit |
| Guardrails      | GuardrailsAI |
| Hosting         | Replit |
| Agents (opt)    | Dust.tt or LangChain agents |
| Workflows (opt) | Flowise |

## ⚡ Quickstart

```bash
git clone https://github.com/yourname/rag-product-starter.git
cd rag-product-starter
pip install -r requirements.txt
cp .env.example .env  # Add your API keys

# Ingest documents
python ingest/ingest_docs.py

# Run the app
streamlit run app/ui.py
