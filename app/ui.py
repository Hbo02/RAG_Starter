## app/ui.py
import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.config 
from rag_guardrails.eval_feedback import guarded_ask

st.set_page_config(page_title="RAG Product Starter")
st.title("🔍 RAG Q&A over Your Docs")

query = st.text_input("Ask a question")

if st.button("Run") and query:
    with st.spinner("Thinking..."):
        answer = guarded_ask(query)
        st.write("### Answer:", answer)
