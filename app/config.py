import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SESSION_TYPE = os.getenv("SESSION_TYPE")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SECRET_KEY = os.getenv("SECRET_KEY")
    SESSION_USE_SIGNER = True
    # DEBUG
    SQLALCHEMY_ECHO = True