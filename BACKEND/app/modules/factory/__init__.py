# BACKEND\app\modules\factory\__init__.py

from .routes.division_routes import division_bp
from .routes.site_routes import site_bp


# On peut centraliser ici les Blueprints du module factory
def register_factory_routes(app, url_prefix="/factory"):
    app.register_blueprint(division_bp, url_prefix=url_prefix)
    app.register_blueprint(site_bp, url_prefix=url_prefix)
