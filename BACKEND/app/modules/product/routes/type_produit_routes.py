# BACKEND/app/modules/product/routes/type_produit_routes.py

from flask import Blueprint, request, jsonify
from app.modules.product.services.type_produit_service import TypeProduitService
from app.modules.product.schema.type_produit.TypeProduitSchema import (
    TypeProduitSchema,
    TypeProduitCreateSchema,
    TypeProduitUpdateSchema,
)

type_produit_bp = Blueprint("type_produit_bp", __name__, url_prefix="/types-produit")
service = TypeProduitService()

# GET /types-produit → liste tous les types de produit
@type_produit_bp.route("/", methods=["GET"])
def get_all_types():
    types = service.get_all()
    schema = TypeProduitSchema(many=True)
    return jsonify(schema.dump(types)), 200

# GET /types-produit/<id> → récupère un type de produit par ID
@type_produit_bp.route("/<string:type_id>", methods=["GET"])
def get_type_produit(type_id):
    type_produit = service.get_by_id(type_id)
    if not type_produit:
        return jsonify({"message": "Type produit not found"}), 404
    schema = TypeProduitSchema()
    return jsonify(schema.dump(type_produit)), 200

# POST /types-produit → crée un nouveau type de produit
@type_produit_bp.route("/", methods=["POST"])
def create_type_produit():
    data = request.get_json()
    schema = TypeProduitCreateSchema()
    validated_data = schema.load(data)
    type_produit = service.create(validated_data)
    return jsonify(TypeProduitSchema().dump(type_produit)), 201

# PUT /types-produit/<id> → met à jour un type de produit
@type_produit_bp.route("/<string:type_id>", methods=["PUT"])
def update_type_produit(type_id):
    data = request.get_json()
    schema = TypeProduitUpdateSchema()
    validated_data = schema.load(data, partial=True)
    type_produit = service.update(type_id, validated_data)
    if not type_produit:
        return jsonify({"message": "Type produit not found"}), 404
    return jsonify(TypeProduitSchema().dump(type_produit)), 200

# DELETE /types-produit/<id> → supprime un type de produit
@type_produit_bp.route("/<string:type_id>", methods=["DELETE"])
def delete_type_produit(type_id):
    success = service.delete(type_id)
    if not success:
        return jsonify({"message": "Type produit not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
