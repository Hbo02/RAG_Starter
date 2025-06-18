## llm/rag_chain.py
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from retriever.faiss_retriever import load_retriever

retriever = load_retriever()
llm = ChatOpenAI(temperature=0)
rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

def ask_rag(query):
    return rag_chain.run(query)
