from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from app.auth.dependencies import get_current_user
from app.dependencies.repositories import get_report_repository
from app.repositories.report_repository import ReportRepository

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/dashboard")
async def dashboard(
    request: Request,
    user=Depends(get_current_user),
    repository: ReportRepository = Depends(get_report_repository)
):

    reports = repository.get_reports(user["email"])

    total_reports = repository.get_total_reports(user["email"])

    avg_match = repository.get_average_match(user["email"])

    highest_match = repository.get_highest_match(user["email"])

    avg_ats = repository.get_average_ats(user["email"])

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "user": user,
            "reports": reports[:5],
            "total_reports": total_reports,
            "avg_match": avg_match,
            "highest_match": highest_match,
            "avg_ats": avg_ats
        }
    )
