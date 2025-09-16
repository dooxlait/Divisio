# BACKEND/app/modules/product/routes/carton_routes.py

from flask import Blueprint, request, jsonify
from app.modules.product.services.carton_service import CartonService
from app.modules.product.schema.carton.CartonSchema import (
    CartonSchema,
    CartonCreateSchema,
    CartonUpdateSchema,
)

carton_bp = Blueprint("carton_bp", __name__, url_prefix="/cartons")
service = CartonService()

# GET /cartons → liste tous les cartons
@carton_bp.route("/", methods=["GET"])
def get_all_cartons():
    cartons = service.get_all()
    schema = CartonSchema(many=True)
    return jsonify(schema.dump(cartons)), 200

# GET /cartons/<id> → récupère un carton par ID
@carton_bp.route("/<string:carton_id>", methods=["GET"])
def get_carton(carton_id):
    carton = service.get_by_id(carton_id)
    if not carton:
        return jsonify({"message": "Carton not found"}), 404
    schema = CartonSchema()
    return jsonify(schema.dump(carton)), 200

# POST /cartons → crée un nouveau carton
@carton_bp.route("/", methods=["POST"])
def create_carton():
    data = request.get_json()
    schema = CartonCreateSchema()
    validated_data = schema.load(data)
    carton = service.create(validated_data)
    return jsonify(CartonSchema().dump(carton)), 201

# PUT /cartons/<id> → met à jour un carton
@carton_bp.route("/<string:carton_id>", methods=["PUT"])
def update_carton(carton_id):
    data = request.get_json()
    schema = CartonUpdateSchema()
    validated_data = schema.load(data, partial=True)
    carton = service.update(carton_id, validated_data)
    if not carton:
        return jsonify({"message": "Carton not found"}), 404
    return jsonify(CartonSchema().dump(carton)), 200

# DELETE /cartons/<id> → supprime un carton
@carton_bp.route("/<string:carton_id>", methods=["DELETE"])
def delete_carton(carton_id):
    success = service.delete(carton_id)
    if not success:
        return jsonify({"message": "Carton not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
