import json

def ask_llm(prompt: str) -> str:
    """
    Simulē LLM atbildi (bez API, bez interneta).
    Vienmēr strādā.
    """

    return json.dumps([
        {
            "title": "Klientu skaits pa mēnešiem",
            "sql_goal": "Parādīt klientu skaitu pa mēnešiem",
            "chart_type": "bar"
        },
        {
            "title": "Pārdošanas tendence",
            "sql_goal": "Parādīt pārdošanas summu pa mēnešiem",
            "chart_type": "line"
        }
    ])