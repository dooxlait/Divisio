# BACKEND/app/modules/product/routes/coiffe_routes.py

from flask import Blueprint, request, jsonify
from app.modules.product.services.coiffe_service import CoiffeService
from app.modules.product.schema.coiffe.CoiffeSchema import (
    CoiffeSchema,
    CoiffeCreateSchema,
    CoiffeUpdateSchema,
)

coiffe_bp = Blueprint("coiffe_bp", __name__, url_prefix="/coiffes")
service = CoiffeService()

# GET /coiffes → liste toutes les coiffes
@coiffe_bp.route("/", methods=["GET"])
def get_all_coiffes():
    coiffes = service.get_all()
    schema = CoiffeSchema(many=True)
    return jsonify(schema.dump(coiffes)), 200

# GET /coiffes/<id> → récupère une coiffe par ID
@coiffe_bp.route("/<string:coiffe_id>", methods=["GET"])
def get_coiffe(coiffe_id):
    coiffe = service.get_by_id(coiffe_id)
    if not coiffe:
        return jsonify({"message": "Coiffe not found"}), 404
    schema = CoiffeSchema()
    return jsonify(schema.dump(coiffe)), 200

# POST /coiffes → crée une nouvelle coiffe
@coiffe_bp.route("/", methods=["POST"])
def create_coiffe():
    data = request.get_json()
    schema = CoiffeCreateSchema()
    validated_data = schema.load(data)
    coiffe = service.create(validated_data)
    return jsonify(CoiffeSchema().dump(coiffe)), 201

# PUT /coiffes/<id> → met à jour une coiffe
@coiffe_bp.route("/<string:coiffe_id>", methods=["PUT"])
def update_coiffe(coiffe_id):
    data = request.get_json()
    schema = CoiffeUpdateSchema()
    validated_data = schema.load(data, partial=True)
    coiffe = service.update(coiffe_id, validated_data)
    if not coiffe:
        return jsonify({"message": "Coiffe not found"}), 404
    return jsonify(CoiffeSchema().dump(coiffe)), 200

# DELETE /coiffes/<id> → supprime une coiffe
@coiffe_bp.route("/<string:coiffe_id>", methods=["DELETE"])
def delete_coiffe(coiffe_id):
    success = service.delete(coiffe_id)
    if not success:
        return jsonify({"message": "Coiffe not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
