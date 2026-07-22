from pymongo import MongoClient

from app.config.settings import settings

client = MongoClient(settings.MONGODB_URI)

db = client[settings.DATABASE_NAME]

users_collection = db["users"]

reports_collection = db["resume_reports"]