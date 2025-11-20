# BACKEND/app/__init__.py

from flask import Flask

from .core.config import DevelopmentConfig
from .core.extensions import db, migrate, ma
from app.core.cors import init_cors
from .common.response.response import error_response


def create_app(config_class=DevelopmentConfig):
    """Application factory"""
    app = Flask(__name__)

    # Charger la configuration
    app.config.from_object(config_class)

    # Initialiser les extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    init_cors(app)

    # Préfixe global pour l'API
    api_prefix = "/api"

    # ------------------------------------------------------------------
    # 1. CHARGER TOUS LES MODÈLES EN PREMIER
    #    (obligatoire pour éviter les erreurs de résolution de relations)
    # ------------------------------------------------------------------
    from app.modules.production import models as production_models
    from app.modules.factory import models as factory_models
    from app.modules.hr import models as hr_models
    from app.modules.machine import models as machine_models
    from app.modules.articles import models as article_models
    # (tu peux ajouter ici d'autres modules si besoin)

    # ------------------------------------------------------------------
    # 2. IMPORTER LES FONCTIONS D'ENREGISTREMENT DES ROUTES
    #    (maintenant que tous les modèles sont chargés, c'est safe)
    # ------------------------------------------------------------------
    from .modules.factory import register_factory_routes
    from .modules.machine import register_machine_routes
    from .modules.hr import register_employee_routes
    from .modules.API import register_API_routes
    from .modules.articles import register_article_routes
    from .modules.statistique import register_statistique_routes
    from .modules.production import register_production_routes

    # ------------------------------------------------------------------
    # 3. ENREGISTRER LES BLUEPRINTS / ROUTES
    # ------------------------------------------------------------------
    register_factory_routes(app, url_prefix=f"{api_prefix}/factory")
    register_machine_routes(app, url_prefix=f"{api_prefix}/machine")
    register_employee_routes(app, url_prefix=f"{api_prefix}/employee")
    register_API_routes(app, url_prefix=f"{api_prefix}/API")
    register_article_routes(app, url_prefix=f"{api_prefix}/article")
    register_statistique_routes(app, url_prefix=f"{api_prefix}/statistique")
    register_production_routes(app, url_prefix=f"{api_prefix}/production")

    # ------------------------------------------------------------------
    # Gestion globale des erreurs HTTP
    # ------------------------------------------------------------------
    @app.errorhandler(404)
    def not_found(e):
        return error_response("Resource not found", 404)

    @app.errorhandler(500)
    def server_error(e):
        return error_response("Internal server error", 500)

    @app.errorhandler(400)
    def bad_request(e):
        return error_response("Bad request", 400)

    return app