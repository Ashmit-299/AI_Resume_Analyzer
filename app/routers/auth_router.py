from datetime import datetime

from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from app.auth.oauth import google
from app.database.database import users_collection

auth_router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@auth_router.get("/login")
async def login(request: Request):
    return templates.TemplateResponse(
        request,
        "login.html",
        {}
    )


@auth_router.get("/test")
async def test(request: Request):
    return templates.TemplateResponse(
        "test.html",
        {
            "request": request
        }
    )


@auth_router.get("/auth/google")
async def auth_google(request: Request):

    redirect_uri = request.url_for("auth_callback")

    return await google.authorize_redirect(
        request,
        redirect_uri
    )


@auth_router.get("/auth/google/callback", name="auth_callback")
async def auth_callback(request: Request):

    token = await google.authorize_access_token(request)

    user_info = token.get("userinfo")

    if user_info is None:

        user_info = await google.parse_id_token(
            request,
            token
        )

    email = user_info["email"]

    existing_user = users_collection.find_one(
        {
            "email": email
        }
    )

    if existing_user:

        users_collection.update_one(
            {
                "email": email
            },
            {
                "$set": {
                    "last_login": datetime.utcnow()
                }
            }
        )

    else:

        users_collection.insert_one(
            {
                "google_id": user_info["sub"],
                "name": user_info["name"],
                "email": user_info["email"],
                "picture": user_info["picture"],
                "created_at": datetime.utcnow(),
                "last_login": datetime.utcnow(),
                "total_reports": 0
            }
        )

    request.session["user"] = {
        "name": user_info["name"],
        "email": user_info["email"],
        "picture": user_info["picture"]
    }

    return RedirectResponse(url="/")


@auth_router.get("/logout")
async def logout(request: Request):

    request.session.clear()

    return RedirectResponse("/login")