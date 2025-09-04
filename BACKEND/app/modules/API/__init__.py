# BACKEND\app\modules\API\__init__.py

from app.modules.API.routes.healthcheck_routes import api_bp

# On peut centraliser ici les Blueprints du module API
def register_API_routes(app, url_prefix="/API"):
    app.register_blueprint(api_bp, url_prefix=url_prefix)