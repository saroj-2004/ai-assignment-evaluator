# Report agent placeholder
from crewai import Agent

report = Agent(
    role="Report Generator",
    goal="Prepare the final evaluation report.",
    backstory="""
    You combine marks and feedback into a final report.
    """,
    llm="ollama/llama3.2",
    verbose=True
)