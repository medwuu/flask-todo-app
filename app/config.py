import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SESSION_TYPE = os.getenv("SESSION_TYPE", "filesystem")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///todo.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "change me")
    SESSION_USE_SIGNER = True
    DEBUG = os.getenv("DEBUG", False)
    SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO", False)