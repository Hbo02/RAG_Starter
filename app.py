## retriever/faiss_retriever.py
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def load_retriever():
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local("faiss_index", embeddings)
    return db

---

## llm/rag_chain.py
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from retriever.faiss_retriever import load_retriever

retriever = load_retriever()
llm = ChatOpenAI(temperature=0)
rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

def ask_rag(query):
    return rag_chain.run(query)

---

## guardrails/safety_rails.gr.xml
<guardrails>
  <output>
    <type>string</type>
    <constraints>
      <length max="1000" />
      <profanity level="moderate" />
    </constraints>
  </output>
</guardrails>

---

## guardrails/eval_feedback.py
from guardrails import Guard
from llm.rag_chain import ask_rag

guard = Guard.from_preset("guardrails/safety_rails.gr.xml")

def guarded_ask(query):
    raw_output = ask_rag(query)
    validated_output = guard.validate(output=raw_output)
    return validated_output.output

---

## app/ui.py
import streamlit as st
from guardrails.eval_feedback import guarded_ask

st.set_page_config(page_title="RAG Product Starter")
st.title("🔍 RAG Q&A over Your Docs")

query = st.text_input("Ask a question")

if st.button("Run") and query:
    with st.spinner("Thinking..."):
        answer = guarded_ask(query)
        st.write("### Answer:", answer)

---

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
