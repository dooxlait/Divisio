#BACKEND\app\core\config.py

import os
from dotenv import load_dotenv

# Charger les variables du .env
load_dotenv()

class Config:
    """Config de base (commune à tous les environnements)"""
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # recommandé pour éviter un warning

class DevelopmentConfig(Config):
    """Config propre au développement"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI", 
        "sqlite:///dev.db"
    )

class ProductionConfig(Config):
    """Config de production"""
    DEBUG = False 
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
