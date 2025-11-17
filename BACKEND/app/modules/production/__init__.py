# BACKEND\app\modules\production\__init__.py

from .routes import production_order_routes

def register_production_routes(app, url_prefix="/production"):
    app.register_blueprint(production_order_routes, url_prefix=f"{url_prefix}/orders")