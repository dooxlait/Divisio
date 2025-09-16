# BACKEND/app/modules/product/routes/format_routes.py

from flask import Blueprint, request, jsonify
from app.modules.product.services.format_service import FormatService
from app.modules.product.schema.format.FormatSchema import (
    FormatSchema,
    FormatCreateSchema,
    FormatUpdateSchema,
)

format_bp = Blueprint("format_bp", __name__, url_prefix="/formats")
service = FormatService()

# GET /formats → liste tous les formats
@format_bp.route("/", methods=["GET"])
def get_all_formats():
    formats = service.get_all()
    schema = FormatSchema(many=True)
    return jsonify(schema.dump(formats)), 200

# GET /formats/<id> → récupère un format par ID
@format_bp.route("/<string:format_id>", methods=["GET"])
def get_format(format_id):
    format_obj = service.get_by_id(format_id)
    if not format_obj:
        return jsonify({"message": "Format not found"}), 404
    schema = FormatSchema()
    return jsonify(schema.dump(format_obj)), 200

# POST /formats → crée un nouveau format
@format_bp.route("/", methods=["POST"])
def create_format():
    data = request.get_json()
    schema = FormatCreateSchema()
    validated_data = schema.load(data)
    format_obj = service.create(validated_data)
    return jsonify(FormatSchema().dump(format_obj)), 201

# PUT /formats/<id> → met à jour un format
@format_bp.route("/<string:format_id>", methods=["PUT"])
def update_format(format_id):
    data = request.get_json()
    schema = FormatUpdateSchema()
    validated_data = schema.load(data, partial=True)
    format_obj = service.update(format_id, validated_data)
    if not format_obj:
        return jsonify({"message": "Format not found"}), 404
    return jsonify(FormatSchema().dump(format_obj)), 200

# DELETE /formats/<id> → supprime un format
@format_bp.route("/<string:format_id>", methods=["DELETE"])
def delete_format(format_id):
    success = service.delete(format_id)
    if not success:
        return jsonify({"message": "Format not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
