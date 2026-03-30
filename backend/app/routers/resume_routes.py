import os
from fastapi import APIRouter, UploadFile, File, Depends, Form
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.resume import Resume
from app.utils.text_extractor import extract_resume_text
from app.utils.analyzer import analyze_resume
from app.utils.matcher import match_resume_with_job
from app.utils.suggestions import generate_suggestions
from app.utils.dependencies import get_current_user
from app.utils.grammar_checker import check_grammar

router = APIRouter()

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@router.post("/upload-resume")
def upload_resume(
    file: UploadFile = File(...),
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    
    file_path = f"{UPLOAD_FOLDER}/{file.filename}"
    
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    text = extract_resume_text(file_path)

    # AI ANALYSIS
    analysis = analyze_resume(text)

    grammar_report = check_grammar(text)

    new_resume = Resume(
        user_id=current_user.id,
        file_name=file.filename,
        extracted_text=text,
        score=analysis["score"]
    )

    db.add(new_resume)
    db.commit()

    return {
        "message": "Resume analyzed successfully",
        "score": analysis["score"],
        "grammer_issues": grammar_report,
        "skills_found": analysis.get("skills_found", [])
    }

@router.post("/match-job")
def match_job(
    job_description: str = Form(...),
    db: Session = Depends(get_db)
):
    resume = db.query(Resume).order_by(Resume.id.desc()).first()

    if not resume:
        return {"message": "No resume found"}

    result = match_resume_with_job(resume.extracted_text, job_description)

    suggestions = generate_suggestions(result["matched_skills"], result["missing_skills"])

    return {
        "message": "Job matching done",
        "match_score": result["match_score"],
        "matched_skills": result["matched_skills"],
        "missing_skills": result["missing_skills"],
        "suggestions": suggestions
    }