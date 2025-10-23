# BACKEND\app\modules\articles\routes\marque_routes.py

from flask import Blueprint, request, jsonify
from app.common.response.response import success_response, error_response

marque_bp = Blueprint('marque_bp', __name__, url_prefix='/marques')

@marque_bp.route("/", methods=["POST"])
def create_marque_route():
    pass

@marque_bp.route("/", methods=["GET"])
def get_all_marques_route():
    pass

@marque_bp.route("/<int:marque_id>", methods=["GET"])
def get_marque_by_id_route(marque_id):
    pass

@marque_bp.route("/<int:marque_id>", methods=["PUT"])
def update_marque_route(marque_id):
    pass
