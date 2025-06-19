## rag_guardrails/eval_feedback.py
from guardrails import Guard
from llm.rag_chain import ask_rag
import utils.config

with open("rag_guardrails/safety_rails.gr.xml", "r", encoding="utf-8-sig") as f:
    content = f.read()
    print("RAIL content:\n", content)
    
guard = Guard.for_rail_string(content)

def guarded_ask(query):
    raw_output = ask_rag(query)
    validated_output = guard.validate(output=raw_output)
    return validated_output.output
