# Assignment Evaluation Agent - Project Summary

## 1. What this project does
This project is an AI-powered assignment evaluation system. It uses multiple agent roles to read an assignment, evaluate it against a rubric, generate feedback, and prepare a final report.

The system is built around CrewAI agents and is exposed through a simple FastAPI API.

---

## 2. Project goal
The main purpose is to automate the process of:
- reading a student assignment,
- judging it according to a rubric,
- giving marks and feedback,
- producing a final evaluation report.

This is useful for educational or academic review workflows.

---

## 3. Main folder structure

### Root folder
- main.py: the API entry point for the application.
- crew_setup.py: connects all agents and tasks into one crew workflow.
- test_crew.py: a sample script to run the evaluation flow directly.
- rubric.json: the rubric and grading instructions used by the evaluator.
- workflow.png: a visual diagram of the workflow.
- read.md: this summary file.

### agents/
This folder contains the AI agents responsible for each stage of the process.
- reader.py: reads and understands the assignment.
- evaluator.py: evaluates the assignment and assigns marks.
- feedback.py: writes constructive feedback for the student.
- report.py: prepares the final report.

### tasks/
- tasks.py: defines the tasks that each agent will perform.

### tools/
- pdf_reader.py: intended for reading PDF assignments, but it is currently a placeholder.
- rubric_loader.py: loads rubric data from rubric.json.

---

## 4. How the system works
The flow is:
1. A user sends assignment details to the app.
2. The reader agent understands the content.
3. The evaluator agent checks the assignment against the rubric.
4. The feedback agent writes remarks and suggestions.
5. The report agent combines everything into a final evaluation report.

The system uses a sequential process, meaning one step follows the other in order.

---

## 5. Important files and what they do

### main.py
This file starts a FastAPI web service.
It exposes:
- GET / : checks whether the API is running
- POST /evaluate : accepts assignment details and runs the full evaluation workflow

Expected input to /evaluate includes:
- assignment: the student’s assignment text
- subject: the subject name
- max_marks: the maximum marks available

### crew_setup.py
This is the orchestration file.
It imports all agents and tasks, creates a Crew, and runs the workflow using sequential processing.

### test_crew.py
This is a quick test script that runs the crew with a sample AI assignment and prints the result.

### rubric.json
This file contains the grading rubric and teacher instructions.
It includes:
- subject name
- course level
- maximum marks
- rubric categories such as correctness, explanation, examples, and grammar
- teacher instructions for strict evaluation

### agents/reader.py
This agent is responsible for understanding the assignment content and extracting the main ideas.

### agents/evaluator.py
This agent evaluates the assignment against the rubric and assigns marks for each category.

### agents/feedback.py
This agent writes supportive and useful feedback for the student.

### agents/report.py
This agent creates the final structured evaluation report.

### tasks/tasks.py
This file defines the actual tasks for the workflow:
- reading task
- evaluation task
- feedback task
- report task

Each task is linked to a specific agent.

### tools/rubric_loader.py
This file reads the rubric.json file and returns its contents to the task system.

### tools/pdf_reader.py
This file is currently a placeholder. It is meant to handle PDF file reading in the future, but it is not fully implemented yet.

---

## 6. How to run the project

### Option 1: Run the sample test
From the project folder, run:
```bash
python test_crew.py
```
This will execute the assignment evaluation flow with a sample input.

### Option 2: Run the API
Start the API with:
```bash
uvicorn main:app --reload
```
Then send a POST request to:
```text
http://127.0.0.1:8000/evaluate
```
Example JSON body:
```json
{
  "assignment": "Artificial Intelligence helps automate repetitive tasks.",
  "subject": "Artificial Intelligence",
  "max_marks": 20
}
```

---

## 7. Current status of the project
The project is in an early stage. The basic structure is working, and the agent-based workflow is set up.

What is already implemented:
- project structure,
- agent definitions,
- task definitions,
- rubric loading,
- API entry point,
- sample execution script.

What is still incomplete or placeholder-based:
- PDF reading is not yet implemented,
- the agents use simple prompts and may need stronger logic or better formatting,
- reporting and feedback can be improved for real-world use.

---

## 8. Simple explanation of the architecture
Think of the project as a small multi-agent system:
- one agent reads,
- one agent evaluates,
- one agent gives feedback,
- one agent writes the report.

These agents work together through a crew, and the whole process is triggered by the main API.

---

## 9. Summary in one sentence
This project is a beginner-friendly AI assignment evaluation system that uses CrewAI agents to read, evaluate, comment on, and report on student assignments.
