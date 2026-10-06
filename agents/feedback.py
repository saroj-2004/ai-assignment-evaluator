# Feedback agent placeholder
from crewai import Agent

feedback = Agent(
    role="Feedback Writer",
    goal="Provide constructive feedback to the student.",
    backstory="""
    You help students improve.
    """,
    llm="ollama/llama3.2",
    verbose=True
)