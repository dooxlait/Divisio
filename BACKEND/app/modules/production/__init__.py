# BACKEND\app\modules\production\__init__.py

def register_production_routes(app, url_prefix="/production"):
    from .routes import production_order_routes, production_recipe_bp
    app.register_blueprint(production_recipe_bp, url_prefix=f"{url_prefix}/recipes")
    app.register_blueprint(production_order_routes, url_prefix=f"{url_prefix}/orders")