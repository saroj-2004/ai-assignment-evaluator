# Reader agent placeholder
from crewai import Agent

reader = Agent(
    role="Assignment Reader",
    goal="Read and understand the student's assignment.",
    backstory="""
    You are an experienced university professor.
    Your responsibility is to carefully read and understand assignments.
    """,
    llm="ollama/llama3.2",
    verbose=True
)