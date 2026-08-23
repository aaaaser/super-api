# config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "TeFa Project Management API")
VERSION = "1.0.0"  # <-- Pastikan variabel VERSION ini ada
APP_ENV = os.getenv("APP_ENV", "development")
PORT = int(os.getenv("PORT", 8000))

# Database Settings
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:postgres@localhost:5432/db_tefa_school"
)

# JWT Settings
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default_secret_key")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")