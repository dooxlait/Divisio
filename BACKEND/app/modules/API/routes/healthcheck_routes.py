# BACKEND/app/modules/API/routes/healthcheck_routes.py
from datetime import datetime

from flask import Blueprint
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

from app.core.extensions import db
from app.common.response.response import success_response, error_response

api_bp = Blueprint("api", __name__)


# --- Fonctions utilitaires ---
def get_current_timestamp():
    return datetime.utcnow().isoformat()

# --- Routes ---
@api_bp.route("/health", methods=["GET"])
def health_check():
    """Simple health check de l'API"""
    return success_response(
        data={"timestamp": get_current_timestamp()},
        message="API is healthy",
        status_code=200
    )


@api_bp.route("/db", methods=["GET"])
def check_db():
    """
    Vérifie la connexion à la base de données et récupère la version Alembic.
    Retourne un message détaillé en cas d'erreur.
    """
    try:
        version, error = get_alembic_version()
        if version:
            return success_response(
                data={"ALEMBIC_VERSION": version},
                message="Database connection OK",
                status_code=200
            )
        else:
            return error_response(
                data={"error": error},
                message="Database connection FAILED",
                status_code=500
            )
    except Exception as e:
        # Attrape toute exception inattendue
        return error_response(
            data={"exception": str(e)},
            message="Database connection FAILED",
            status_code=500
        )

def get_alembic_version() -> tuple[str | None, str | None]:
    """
    Essaie de récupérer la version Alembic.
    Retourne un tuple : (version, erreur)
    """
    try:
        result = db.session.execute(text("SELECT version_num FROM alembic_version")).first()
        if result:
            return result[0], None
        else:
            return None, "Table alembic_version vide ou inexistante"
    except Exception as e:
        return None, str(e)
