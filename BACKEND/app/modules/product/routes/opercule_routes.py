# BACKEND/app/modules/product/routes/opercule_routes.py

from flask import Blueprint, request, jsonify
from app.modules.product.services.opercule_service import OperculeService
from app.modules.product.schema.opercule.OperculeSchema import (
    OperculeSchema,
    OperculeCreateSchema,
    OperculeUpdateSchema,
)

opercule_bp = Blueprint("opercule_bp", __name__, url_prefix="/opercules")
service = OperculeService()

# GET /opercules → liste tous les opercules
@opercule_bp.route("/", methods=["GET"])
def get_all_opercules():
    opercules = service.get_all()
    schema = OperculeSchema(many=True)
    return jsonify(schema.dump(opercules)), 200

# GET /opercules/<id> → récupère un opercule par ID
@opercule_bp.route("/<string:opercule_id>", methods=["GET"])
def get_opercule(opercule_id):
    opercule = service.get_by_id(opercule_id)
    if not opercule:
        return jsonify({"message": "Opercule not found"}), 404
    schema = OperculeSchema()
    return jsonify(schema.dump(opercule)), 200

# POST /opercules → crée un nouvel opercule
@opercule_bp.route("/", methods=["POST"])
def create_opercule():
    data = request.get_json()
    schema = OperculeCreateSchema()
    validated_data = schema.load(data)
    opercule = service.create(validated_data)
    return jsonify(OperculeSchema().dump(opercule)), 201

# PUT /opercules/<id> → met à jour un opercule
@opercule_bp.route("/<string:opercule_id>", methods=["PUT"])
def update_opercule(opercule_id):
    data = request.get_json()
    schema = OperculeUpdateSchema()
    validated_data = schema.load(data, partial=True)
    opercule = service.update(opercule_id, validated_data)
    if not opercule:
        return jsonify({"message": "Opercule not found"}), 404
    return jsonify(OperculeSchema().dump(opercule)), 200

# DELETE /opercules/<id> → supprime un opercule
@opercule_bp.route("/<string:opercule_id>", methods=["DELETE"])
def delete_opercule(opercule_id):
    success = service.delete(opercule_id)
    if not success:
        return jsonify({"message": "Opercule not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
