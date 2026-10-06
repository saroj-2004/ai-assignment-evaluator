from crewai import Crew, Process

from agents.reader import reader
from agents.evaluator import evaluator
from agents.feedback import feedback
from agents.report import report

from tasks.tasks import create_tasks


def run_crew(assignment, subject, max_marks):

    tasks = create_tasks(
        assignment,
        subject,
        max_marks
    )

    crew = Crew(

        agents=[
            reader,
            evaluator,
            feedback,
            report
        ],

        tasks=tasks,

        process=Process.sequential,

        verbose=True

    )

    result = crew.kickoff()

    return str(result)