# BACKEND\app\modules\machine\__init__.py

from .routes import machine_bp

# On peut centraliser ici les Blueprints du module machine
def register_machine_routes(app, url_prefix="/machine"):
    app.register_blueprint(machine_bp, url_prefix=url_prefix)
