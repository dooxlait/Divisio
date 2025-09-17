# BACKEND/app/modules/product/routes/pot_routes.py

from flask import Blueprint, request, jsonify
from app.modules.product.services.pot_service import PotService
from app.modules.product.schema.pot.PotSchema import PotSchema
from app.modules.product.schema.pot.PotCreateSchema import PotCreateSchema
from app.modules.product.schema.pot.PotUpdateSchema import PotUpdateSchema


pot_bp = Blueprint("pot_bp", __name__, url_prefix="/pots")
service = PotService()

# GET /pots → liste tous les pots
@pot_bp.route("/", methods=["GET"])
def get_all_pots():
    pots = service.get_all()
    schema = PotSchema(many=True)
    return jsonify(schema.dump(pots)), 200

# GET /pots/<id> → récupère un pot par ID
@pot_bp.route("/<string:pot_id>", methods=["GET"])
def get_pot(pot_id):
    pot = service.get_by_id(pot_id)
    if not pot:
        return jsonify({"message": "Pot not found"}), 404
    schema = PotSchema()
    return jsonify(schema.dump(pot)), 200

# POST /pots → crée un nouveau pot
@pot_bp.route("/", methods=["POST"])
def create_pot():
    data = request.get_json()
    schema = PotCreateSchema()
    validated_data = schema.load(data)
    pot = service.create(validated_data)
    return jsonify(PotSchema().dump(pot)), 201

# PUT /pots/<id> → met à jour un pot
@pot_bp.route("/<string:pot_id>", methods=["PUT"])
def update_pot(pot_id):
    data = request.get_json()
    schema = PotUpdateSchema()
    validated_data = schema.load(data, partial=True)
    pot = service.update(pot_id, validated_data)
    if not pot:
        return jsonify({"message": "Pot not found"}), 404
    return jsonify(PotSchema().dump(pot)), 200

# DELETE /pots/<id> → supprime un pot
@pot_bp.route("/<string:pot_id>", methods=["DELETE"])
def delete_pot(pot_id):
    success = service.delete(pot_id)
    if not success:
        return jsonify({"message": "Pot not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
