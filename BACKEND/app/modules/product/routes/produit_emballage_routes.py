# BACKEND/app/modules/product/routes/produit_emballage_routes.py

from flask import Blueprint, request, jsonify
from app.modules.product.services.produit_emballage_service import ProduitEmballageService
from app.modules.product.schema.produit_emballage.ProduitEmballageSchema import ProduitEmballageSchema
from app.modules.product.schema.produit_emballage.ProduitEmballageCreateSchema import ProduitEmballageCreateSchema
from app.modules.product.schema.produit_emballage.ProduitEmballageUpdateSchema import ProduitEmballageUpdateSchema

produit_emballage_bp = Blueprint("produit_emballage_bp", __name__, url_prefix="/produits-emballage")
service = ProduitEmballageService()

# GET /produits-emballage → liste tous les produits emballage
@produit_emballage_bp.route("/", methods=["GET"])
def get_all_produits_emballage():
    produits = service.get_all()
    schema = ProduitEmballageSchema(many=True)
    return jsonify(schema.dump(produits)), 200

# GET /produits-emballage/<id> → récupère un produit emballage par ID
@produit_emballage_bp.route("/<string:produit_id>", methods=["GET"])
def get_produit_emballage(produit_id):
    produit = service.get_by_id(produit_id)
    if not produit:
        return jsonify({"message": "Produit emballage not found"}), 404
    schema = ProduitEmballageSchema()
    return jsonify(schema.dump(produit)), 200

# POST /produits-emballage → crée un nouveau produit emballage
@produit_emballage_bp.route("/", methods=["POST"])
def create_produit_emballage():
    data = request.get_json()
    schema = ProduitEmballageCreateSchema()
    validated_data = schema.load(data)
    produit = service.create(validated_data)
    return jsonify(ProduitEmballageSchema().dump(produit)), 201

# PUT /produits-emballage/<id> → met à jour un produit emballage
@produit_emballage_bp.route("/<string:produit_id>", methods=["PUT"])
def update_produit_emballage(produit_id):
    data = request.get_json()
    schema = ProduitEmballageUpdateSchema()
    validated_data = schema.load(data, partial=True)
    produit = service.update(produit_id, validated_data)
    if not produit:
        return jsonify({"message": "Produit emballage not found"}), 404
    return jsonify(ProduitEmballageSchema().dump(produit)), 200

# DELETE /produits-emballage/<id> → supprime un produit emballage
@produit_emballage_bp.route("/<string:produit_id>", methods=["DELETE"])
def delete_produit_emballage(produit_id):
    success = service.delete(produit_id)
    if not success:
        return jsonify({"message": "Produit emballage not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
