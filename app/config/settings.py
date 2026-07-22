from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    MONGODB_URI = os.getenv("MONGODB_URI")
    DATABASE_NAME = os.getenv("DATABASE_NAME")

    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

    SECRET_KEY = os.getenv("SECRET_KEY")

    UPLOAD_FOLDER = "uploads"
    MAX_UPLOAD_SIZE = 5 * 1024 * 1024
    MODEL_NAME = "all-MiniLM-L6-v2"
    ALLOWED_EXTENSIONS = ["pdf"]
    REPORT_FOLDER = "reports"


settings = Settings()