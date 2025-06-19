## llm/rag_chain.py
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from retriever.faiss_retriever import load_retriever
import utils.config 
from utils.config import get_env_var

openai_api_key=get_env_var("OPENAI_API_KEY")

retriever = load_retriever()
llm = ChatOpenAI(temperature=0, openai_api_key = openai_api_key)
rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

def ask_rag(query):
    return rag_chain.run(query)
