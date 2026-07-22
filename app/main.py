from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from app.api.routes import router
from app.routers.auth_router import auth_router
from app.routers.history_router import history_router
from app.routers.dashboard_router import router as dashboard_router
from app.routers.report_router import router as report_router
from app.routers.compare_router import router as compare_router
from app.config.settings import settings
from app.services.resume_analysis_service import ResumeAnalysisService

resume_service = None


@asynccontextmanager
async def lifespan(app: FastAPI):

    global resume_service

    print("Loading AI Models...")

    resume_service = ResumeAnalysisService()

    print("Loaded Successfully.")

    yield

    print("Application Shutdown.")

app = FastAPI(
    title="TalentLens AI",
    lifespan=lifespan
)

# Session Middleware
app.add_middleware(
    SessionMiddleware,
    secret_key=settings.SECRET_KEY
)

# Static Files
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

# Routers
app.include_router(auth_router)

app.include_router(router)

app.include_router(history_router)

app.include_router(dashboard_router)

app.include_router(report_router)

app.include_router(compare_router)