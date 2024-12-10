from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    # Security key for signing cookies, sessions, and CSRF protection
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback_default_secret_key")

    # Additional configurations (optional)
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    TESTING = os.getenv("TESTING", "False").lower() == "true"
