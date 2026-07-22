from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException, Request
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import List

from app.auth.dependencies import get_current_user
from app.dependencies.repositories import get_report_repository
from app.services.analysis_workflow import AnalysisWorkflow
from app.core.logger import logger
from app.core.exceptions import ResumeAnalysisException
from app.config.settings import settings
from app.repositories.report_repository import ReportRepository

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

workflow = AnalysisWorkflow()


@router.get("/")
async def home(request: Request):

    if "user" not in request.session:

        return RedirectResponse("/login")

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "user": request.session["user"]
        }
    )


@router.post("/analyze")
async def analyze_resume(
    request: Request,
    user=Depends(get_current_user),
    resume: UploadFile = File(...),
    job_description: str = Form(...),
    repository: ReportRepository = Depends(get_report_repository)
):

    if resume.content_type != "application/pdf":

        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    content = await resume.read()

    if len(content) > settings.MAX_UPLOAD_SIZE:

        raise HTTPException(
            status_code=400,
            detail="Maximum file size is 5MB."
        )

    try:

        result = workflow.analyze_resume(
            file_content=content,
            original_filename=resume.filename,
            user_email=user["email"],
            job_description=job_description
        )

        return result

    except ResumeAnalysisException as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/download-report")
async def download_report(data: dict):

    try:

        pdf_path = workflow.generate_report(data)

        return FileResponse(
            path=pdf_path,
            media_type="application/pdf",
            filename=pdf_path.name
        )

    except ResumeAnalysisException as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
