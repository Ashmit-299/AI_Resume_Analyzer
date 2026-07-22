from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from app.auth.dependencies import get_current_user
from app.dependencies.repositories import get_report_repository
from app.repositories.report_repository import ReportRepository

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/report/{report_id}")
async def report_details(
    report_id: str,
    request: Request,
    user=Depends(get_current_user),
    repository: ReportRepository = Depends(get_report_repository)
):

    report = repository.get_report_by_id(report_id)

    if report is None:

        return RedirectResponse("/history")

    if report["user_email"] != user["email"]:

        return RedirectResponse("/history")

    return templates.TemplateResponse(
        "report.html",
        {
            "request": request,
            "user": user,
            "report": report
        }
    )
