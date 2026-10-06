# Task definitions placeholder
from crewai import Task
from tools.rubric_loader import load_rubric
from agents.reader import reader
from agents.evaluator import evaluator
from agents.feedback import feedback
from agents.report import report


def create_tasks(assignment, subject, max_marks):
    rubric = load_rubric()
    read_task = Task(
    description=f"""
    Read and understand the student's assignment.
    
    Subject:
    {subject}
    
    Assignment:
    {assignment}
    
    Identify:
    - Main topic
    - Important concepts
    - Missing concepts
    - Overall understanding
    """,
        expected_output="Structured analysis of the assignment.",
        agent=reader
    )


    evaluate_task = Task(
    description=f"""
    Evaluate the assignment using the university rubric.
    
    Course Level:
    {rubric['course_level']}
    
    Teacher Instruction:
    {rubric['teacher_instruction']}
    
    Rubric:
    {rubric['rubric']}
    
    Maximum Marks:
    {max_marks}
    
    Give:
    
    1. Marks for each criterion
    2. Total Marks
    3. Strengths
    4. Weaknesses
    5. Justification
    """,
        expected_output="Detailed evaluation with marks.",
        agent=evaluator,
        context=[read_task]
    )


    feedback_task = Task(
    description="""
    Using the evaluator's result, write constructive feedback.
    
    Include:
    
    - Positive points
    - Weak points
    - Suggestions
    - Final advice
    """,
        expected_output="Detailed feedback.",
        agent=feedback,
        context=[evaluate_task]
    )
    
    
    report_task = Task(
    description="""
    Create a professional university evaluation report.
    
    The report must contain:
    
    # Assignment Evaluation Report
    
    ## Subject
    
    ## Assignment Summary
    
    ## Marks
    
    ## Strengths
    
    ## Weaknesses
    
    ## Feedback
    
    ## Final Recommendation
    
    Format everything nicely.
    """,
        expected_output="Professional report.",
        agent=report,
        context=[
            read_task,
            evaluate_task,
            feedback_task
        ]
    )
    
    return [
    read_task,
    evaluate_task,
    feedback_task,
    report_task
]