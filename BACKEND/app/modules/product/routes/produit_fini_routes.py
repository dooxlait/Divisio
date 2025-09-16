# BACKEND/app/modules/product/routes/produit_fini_routes.py

from flask import Blueprint, request, jsonify
from app.modules.product.services.produit_fini_service import ProduitFiniService
from app.modules.product.schema.produit_fini.ProduitFiniSchema import (
    ProduitFiniSchema,
    ProduitFiniCreateSchema,
    ProduitFiniUpdateSchema,
)

produit_fini_bp = Blueprint("produit_fini_bp", __name__, url_prefix="/produits-fini")
service = ProduitFiniService()

# GET /produits-fini → liste tous les produits finis
@produit_fini_bp.route("/", methods=["GET"])
def get_all_produits_fini():
    produits = service.get_all()
    schema = ProduitFiniSchema(many=True)
    return jsonify(schema.dump(produits)), 200

# GET /produits-fini/<id> → récupère un produit fini par ID
@produit_fini_bp.route("/<string:produit_id>", methods=["GET"])
def get_produit_fini(produit_id):
    produit = service.get_by_id(produit_id)
    if not produit:
        return jsonify({"message": "Produit fini not found"}), 404
    schema = ProduitFiniSchema()
    return jsonify(schema.dump(produit)), 200

# POST /produits-fini → crée un nouveau produit fini
@produit_fini_bp.route("/", methods=["POST"])
def create_produit_fini():
    data = request.get_json()
    schema = ProduitFiniCreateSchema()
    validated_data = schema.load(data)
    produit = service.create(validated_data)
    return jsonify(ProduitFiniSchema().dump(produit)), 201

# PUT /produits-fini/<id> → met à jour un produit fini
@produit_fini_bp.route("/<string:produit_id>", methods=["PUT"])
def update_produit_fini(produit_id):
    data = request.get_json()
    schema = ProduitFiniUpdateSchema()
    validated_data = schema.load(data, partial=True)
    produit = service.update(produit_id, validated_data)
    if not produit:
        return jsonify({"message": "Produit fini not found"}), 404
    return jsonify(ProduitFiniSchema().dump(produit)), 200

# DELETE /produits-fini/<id> → supprime un produit fini
@produit_fini_bp.route("/<string:produit_id>", methods=["DELETE"])
def delete_produit_fini(produit_id):
    success = service.delete(produit_id)
    if not success:
        return jsonify({"message": "Produit fini not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
