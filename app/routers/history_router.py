from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from app.dependencies.repositories import get_report_repository
from app.repositories.report_repository import ReportRepository

history_router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@history_router.get("/history")
async def history(
    request: Request,
    repository: ReportRepository = Depends(get_report_repository)
):

    if "user" not in request.session:

        return RedirectResponse("/login")

    reports = repository.get_reports(
        request.session["user"]["email"]
    )

    return templates.TemplateResponse(
        "history.html",
        {
            "request": request,
            "reports": reports,
            "user": request.session["user"]
        }
    )
