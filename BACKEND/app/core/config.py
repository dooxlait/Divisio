#BACKEND\app\core\config.py

import os
from dotenv import load_dotenv

# Charger les variables du .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    EXPORT_DIR = os.getenv("EXPORT_DIR", "RESSOURCES/Export")  # valeur par défaut

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///dev.db")

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
