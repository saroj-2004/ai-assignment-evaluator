from fastapi import FastAPI
from pydantic import BaseModel

from crew_setup import run_crew

from fastapi import UploadFile, File

from tools.pdf_reader import extract_text

from tools.pdf_report import generate_report
from fastapi.responses import FileResponse

from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/reports", StaticFiles(directory="reports"), name="reports")

class Assignment(BaseModel):
    assignment: str
    subject: str
    max_marks: int


@app.get("/")
def home():
    return {"message": "Assignment Evaluation API is running"}


@app.post("/evaluate")
def evaluate(data: Assignment):

    result = run_crew(
        assignment=data.assignment,
        subject=data.subject,
        max_marks=data.max_marks
    )

    pdf = generate_report(result)

    return {
        "result": result,
        "report": pdf
}
    
@app.post("/evaluate-pdf")
def evaluate_pdf(file: UploadFile = File(...)):

    pdf_path = file.filename

    contents = file.file.read()

    with open(pdf_path, "wb") as f:
        f.write(contents)

    assignment = extract_text(pdf_path)

    result = run_crew(
        assignment=assignment,
        subject="Artificial Intelligence",
        max_marks=20
    )
    pdf = generate_report(result)
    return {
        "assignment": assignment,
        "result": result,
        "report": pdf_path
    }
    
from fastapi.responses import FileResponse
import os

@app.get("/download/{filename}")
def download_report(filename: str):

    filepath = os.path.join("reports", filename)

    if not os.path.exists(filepath):
        return {"error": "Report not found"}

    return FileResponse(
        path=filepath,
        media_type="application/pdf",
        filename=filename
    )
