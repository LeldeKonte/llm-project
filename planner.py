import json
from llm import ask_llm

def create_plan(user_context):

    prompt = f"""
Izveido datu analīzes plānu:

{user_context}
"""

    result = ask_llm(prompt)

    return json.loads(result)