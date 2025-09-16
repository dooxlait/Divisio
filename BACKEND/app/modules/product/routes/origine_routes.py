# BACKEND/app/modules/product/routes/origine_routes.py

from flask import Blueprint, request, jsonify
from app.modules.product.services.origine_service import OrigineService
from app.modules.product.schema.origine.OrigineSchema import (
    OrigineSchema,
    OrigineCreateSchema,
    OrigineUpdateSchema,
)

origine_bp = Blueprint("origine_bp", __name__, url_prefix="/origines")
service = OrigineService()

# GET /origines → liste toutes les origines
@origine_bp.route("/", methods=["GET"])
def get_all_origines():
    origines = service.get_all()
    schema = OrigineSchema(many=True)
    return jsonify(schema.dump(origines)), 200

# GET /origines/<id> → récupère une origine par ID
@origine_bp.route("/<string:origine_id>", methods=["GET"])
def get_origine(origine_id):
    origine = service.get_by_id(origine_id)
    if not origine:
        return jsonify({"message": "Origine not found"}), 404
    schema = OrigineSchema()
    return jsonify(schema.dump(origine)), 200

# POST /origines → crée une nouvelle origine
@origine_bp.route("/", methods=["POST"])
def create_origine():
    data = request.get_json()
    schema = OrigineCreateSchema()
    validated_data = schema.load(data)
    origine = service.create(validated_data)
    return jsonify(OrigineSchema().dump(origine)), 201

# PUT /origines/<id> → met à jour une origine
@origine_bp.route("/<string:origine_id>", methods=["PUT"])
def update_origine(origine_id):
    data = request.get_json()
    schema = OrigineUpdateSchema()
    validated_data = schema.load(data, partial=True)
    origine = service.update(origine_id, validated_data)
    if not origine:
        return jsonify({"message": "Origine not found"}), 404
    return jsonify(OrigineSchema().dump(origine)), 200

# DELETE /origines/<id> → supprime une origine
@origine_bp.route("/<string:origine_id>", methods=["DELETE"])
def delete_origine(origine_id):
    success = service.delete(origine_id)
    if not success:
        return jsonify({"message": "Origine not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
