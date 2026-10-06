# Assignment Evaluation Agent

An AI-powered assignment evaluation system that uses a multi-agent workflow to read a student submission, assess it against a rubric, generate feedback, and produce a final evaluation report.

## Overview

This project is designed to automate academic or educational review workflows. It combines:

- CrewAI agents for role-based reasoning
- FastAPI for a simple web API
- JSON rubric configuration for evaluation criteria
- PDF reporting for generated evaluation output

The system follows a sequential workflow:

1. Read the assignment
2. Evaluate it using rubric criteria
3. Generate constructive feedback
4. Compile the final evaluation report

## Features

- Assignment evaluation through specialized AI agents
- Subject-aware rubric-based grading
- Automatic feedback generation
- Final report export in PDF format
- FastAPI endpoints for evaluation requests
- Sample execution script for quick testing

## Project Structure

```text
Assignment-agent/
├── agents/
│   ├── evaluator.py
│   ├── feedback.py
│   ├── reader.py
│   └── report.py
├── tasks/
│   └── tasks.py
├── tools/
│   ├── pdf_reader.py
│   ├── pdf_report.py
│   ├── rubric_loader.py
│   └── __init__.py
├── reports/
├── website/
├── main.py
├── crew_setup.py
├── rubric.json
├── test_crew.py
├── workflow.png
├── read.md
├── assignment.pdf
├── LLM_Finetuning.ipynb
└── README.md
```

## Key Components

### API entry point

`main.py` starts the FastAPI application and exposes endpoints for evaluation.

Endpoints:

- `GET /` — health check
- `POST /evaluate` — evaluate assignment text
- `POST /evaluate-pdf` — evaluate a PDF upload
- `GET /download/{filename}` — download the generated PDF report

### Agent orchestration

`crew_setup.py` creates the Crew and connects all agents and tasks in a sequential process.

### Agents

- `reader`: interprets the assignment content
- `evaluator`: scores the work against rubric criteria
- `feedback`: writes constructive, actionable feedback
- `report`: combines the findings into a final summary

### Rubric

`rubric.json` stores the grading rubric and evaluation instructions. The evaluator uses it to assess correctness, quality, clarity, and subject-specific standards.

## Tech Stack

- Python
- FastAPI
- Pydantic
- CrewAI
- PDF generation/reporting utilities

## Installation

1. Open a terminal in the project folder.
2. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install the project dependencies:

```bash
pip install -r requirements.txt
```

If a `requirements.txt` file is not present in your environment, install the required packages manually, including:

```bash
pip install fastapi uvicorn crewai pydantic python-dotenv
```

## Running the Project

### 1. Run the sample test

```bash
python test_crew.py
```

This executes the assignment evaluation flow with a sample assignment and prints the result.

### 2. Start the API server

```bash
uvicorn main:app --reload
```

Then send requests to the API at:

```text
http://127.0.0.1:8000
```

### Example request

```json
{
  "assignment": "Artificial Intelligence helps automate repetitive tasks and improves decision-making in many fields.",
  "subject": "Artificial Intelligence",
  "max_marks": 20
}
```

Send this to:

```text
POST /evaluate
```

## Example Workflow

The application works like this:

1. User submits an assignment and subject
2. The `reader` agent processes the content
3. The `evaluator` agent validates it against the rubric
4. The `feedback` agent creates a performance summary
5. The `report` agent produces the final evaluation output
6. The app generates a PDF report and returns the result

## Current Status

This project is a functional prototype with a clear multi-agent architecture. It already includes:

- agent-based evaluation workflow
- rubric-driven scoring
- API layer
- sample execution script
- report generation support

The following areas may still require improvement:

- more robust PDF extraction and handling
- stronger grading prompts and output formatting
- production-ready validation and error handling
- more advanced report customization

## License

This project does not currently declare a formal license file. Please check with the repository owner before commercial or public reuse.

## Notes

The project includes a summary document in `read.md`, which may serve as a lightweight design overview for the original implementation.
