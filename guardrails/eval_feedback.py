## guardrails/eval_feedback.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from guardrails import Guard
from llm.rag_chain import ask_rag

guard = Guard.from_preset("guardrails/safety_rails.gr.xml")

def guarded_ask(query):
    raw_output = ask_rag(query)
    validated_output = guard.validate(output=raw_output)
    return validated_output.output
