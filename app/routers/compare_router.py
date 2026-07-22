from fastapi import APIRouter, Depends, Request, Form
from fastapi.templating import Jinja2Templates

from app.auth.dependencies import get_current_user
from app.dependencies.repositories import get_report_repository
from app.repositories.report_repository import ReportRepository

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.post("/compare")
async def compare_candidates(
    request: Request,
    report_ids: list[str] = Form(...),
    user=Depends(get_current_user),
    repository: ReportRepository = Depends(get_report_repository)
):

    reports = repository.compare_reports(report_ids)

    return templates.TemplateResponse(
        "compare.html",
        {
            "request": request,
            "reports": reports,
            "user": user
        }
    )
