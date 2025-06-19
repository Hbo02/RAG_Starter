## rag_guardrails/eval_feedback.py
from guardrails import Guard
from llm.rag_chain import ask_rag
import utils.config

guard = Guard.for_rail("rag_guardrails/safety_rails.gr.xml")

def guarded_ask(query):
    raw_output = ask_rag(query)
    validated_output = guard.validate(output=raw_output)
    return validated_output.output
