# BACKEND\app\modules\hr\__init__.py

from .routes.employee_routes import employee_bp
from .routes.divisionemployee_routes import divisionemployee_bp

# On peut centraliser ici les Blueprints du module Employee
def register_employee_routes(app, url_prefix="/employees"):
    app.register_blueprint(employee_bp, url_prefix=url_prefix)
    app.register_blueprint(divisionemployee_bp, url_prefix=url_prefix)

