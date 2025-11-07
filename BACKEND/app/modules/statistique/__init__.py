# BACKEND\app\modules\statistique\__init__.py

from .routes import statistique_bp

def register_statistique_routes(app, url_prefix="/statistique"):
    app.register_blueprint(statistique_bp, url_prefix=f"{url_prefix}")