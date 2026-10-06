# Evaluator agent placeholder
from crewai import Agent

evaluator = Agent(
    role="Assignment Evaluator",
    goal="Evaluate the assignment and assign marks.",
    backstory="""
    You are a university examiner.
    You evaluate assignments fairly according to the rubric.
    """,
    llm="ollama/llama3.2",
    verbose=True
)