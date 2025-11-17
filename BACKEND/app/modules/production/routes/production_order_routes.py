from flask import Blueprint
from app.common.response.response import success_response, error_response

production_order_routes = Blueprint('production_order_routes', __name__)

@production_order_routes.route('/production_orders', methods=['GET'])
def get_production_orders():
    return success_response(
        data={"orders": []},
        message="Liste des ordres de production récupérée avec succès",
        status_code=200
    )
    
@production_order_routes.route('/production_orders', methods=['POST'])
def create_production_order():
    pass  # Logique de création d'un ordre de production