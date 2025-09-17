# BACKEND/app/modules/product/routes/variante_routes.py

from flask import Blueprint, request, jsonify
from app.modules.product.services.variante_service import VarianteService
from app.modules.product.schema.variante.VarianteSchema import VarianteSchema
from app.modules.product.schema.variante.VarianteCreateSchema import VarianteCreateSchema
from app.modules.product.schema.variante.VarianteUpdateSchema import VarianteUpdateSchema

variante_bp = Blueprint("variante_bp", __name__, url_prefix="/variantes")
service = VarianteService()

# GET /variantes → liste toutes les variantes
@variante_bp.route("/", methods=["GET"])
def get_all_variantes():
    variantes = service.get_all()
    schema = VarianteSchema(many=True)
    return jsonify(schema.dump(variantes)), 200

# GET /variantes/<id> → récupère une variante par ID
@variante_bp.route("/<string:variante_id>", methods=["GET"])
def get_variante(variante_id):
    variante = service.get_by_id(variante_id)
    if not variante:
        return jsonify({"message": "Variante not found"}), 404
    schema = VarianteSchema()
    return jsonify(schema.dump(variante)), 200

# POST /variantes → crée une nouvelle variante
@variante_bp.route("/", methods=["POST"])
def create_variante():
    data = request.get_json()
    schema = VarianteCreateSchema()
    validated_data = schema.load(data)
    variante = service.create(validated_data)
    return jsonify(VarianteSchema().dump(variante)), 201

# PUT /variantes/<id> → met à jour une variante
@variante_bp.route("/<string:variante_id>", methods=["PUT"])
def update_variante(variante_id):
    data = request.get_json()
    schema = VarianteUpdateSchema()
    validated_data = schema.load(data, partial=True)
    variante = service.update(variante_id, validated_data)
    if not variante:
        return jsonify({"message": "Variante not found"}), 404
    return jsonify(VarianteSchema().dump(variante)), 200

# DELETE /variantes/<id> → supprime une variante
@variante_bp.route("/<string:variante_id>", methods=["DELETE"])
def delete_variante(variante_id):
    success = service.delete(variante_id)
    if not success:
        return jsonify({"message": "Variante not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
