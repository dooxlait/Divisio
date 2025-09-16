# BACKEND/app/modules/product/routes/produit_carton_routes.py

from flask import Blueprint, request, jsonify
from app.modules.product.services.produit_carton_service import ProduitCartonService
from app.modules.product.schema.ProduitCarton.ProduitCartonSchema import (
    ProduitCartonSchema,
)

produit_carton_bp = Blueprint("produit_carton_bp", __name__, url_prefix="/produits-carton")
service = ProduitCartonService()

# GET /produits-carton → liste tous les produits carton
@produit_carton_bp.route("/", methods=["GET"])
def get_all_produits_carton():
    produits = service.get_all()
    schema = ProduitCartonSchema(many=True)
    return jsonify(schema.dump(produits)), 200

# GET /produits-carton/<id> → récupère un produit carton par ID
@produit_carton_bp.route("/<string:produit_id>", methods=["GET"])
def get_produit_carton(produit_id):
    produit = service.get_by_id(produit_id)
    if not produit:
        return jsonify({"message": "Produit carton not found"}), 404
    schema = ProduitCartonSchema()
    return jsonify(schema.dump(produit)), 200

# POST /produits-carton → crée un nouveau produit carton
@produit_carton_bp.route("/", methods=["POST"])
def create_produit_carton():
    data = request.get_json()
    schema = ProduitCartonSchema()
    validated_data = schema.load(data)
    produit = service.create(validated_data)
    return jsonify(ProduitCartonSchema().dump(produit)), 201

# PUT /produits-carton/<id> → met à jour un produit carton
@produit_carton_bp.route("/<string:produit_id>", methods=["PUT"])
def update_produit_carton(produit_id):
    data = request.get_json()
    schema = ProduitCartonSchema()
    validated_data = schema.load(data, partial=True)
    produit = service.update(produit_id, validated_data)
    if not produit:
        return jsonify({"message": "Produit carton not found"}), 404
    return jsonify(ProduitCartonSchema().dump(produit)), 200

# DELETE /produits-carton/<id> → supprime un produit carton
@produit_carton_bp.route("/<string:produit_id>", methods=["DELETE"])
def delete_produit_carton(produit_id):
    success = service.delete(produit_id)
    if not success:
        return jsonify({"message": "Produit carton not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
