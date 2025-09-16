# BACKEND/app/modules/product/routes/carton_palette_routes.py

from flask import Blueprint, request, jsonify
from app.modules.product.services.cartonPaletteService import CartonPaletteService
from app.modules.product.schema.carton_palette.CartonPaletteSchema import CartonPaletteSchema
from app.modules.product.schema.carton_palette.CartonPaletteCreateSchema import CartonPaletteCreateSchema
from app.modules.product.schema.carton_palette.CartonPaletteUpdateSchema import CartonPaletteUpdateSchema

carton_palette_bp = Blueprint("carton_palette_bp", __name__, url_prefix="/carton_palette")
service = CartonPaletteService()

# GET /carton_palette/ → liste toutes les associations
@carton_palette_bp.route("/", methods=["GET"])
def get_all():
    result = service.get_all()
    schema = CartonPaletteSchema(many=True)
    return jsonify(schema.dump(result)), 200

# GET /carton_palette/<id> → récupère une association par ID
@carton_palette_bp.route("/<string:cp_id>", methods=["GET"])
def get_by_id(cp_id):
    cp = service.get_by_id(cp_id)
    if not cp:
        return jsonify({"message": "CartonPalette not found"}), 404
    schema = CartonPaletteSchema()
    return jsonify(schema.dump(cp)), 200

# POST /carton_palette/ → crée une nouvelle association
@carton_palette_bp.route("/", methods=["POST"])
def create():
    data = request.get_json()
    schema = CartonPaletteCreateSchema()
    validated_data = schema.load(data)
    cp = service.create(validated_data)
    return jsonify(CartonPaletteSchema().dump(cp)), 201

# PUT /carton_palette/<id> → met à jour une association
@carton_palette_bp.route("/<string:cp_id>", methods=["PUT"])
def update(cp_id):
    data = request.get_json()
    schema = CartonPaletteUpdateSchema()
    validated_data = schema.load(data, partial=True)
    cp = service.update(cp_id, validated_data)
    if not cp:
        return jsonify({"message": "CartonPalette not found"}), 404
    return jsonify(CartonPaletteSchema().dump(cp)), 200

# DELETE /carton_palette/<id> → supprime une association
@carton_palette_bp.route("/<string:cp_id>", methods=["DELETE"])
def delete(cp_id):
    success = service.delete(cp_id)
    if not success:
        return jsonify({"message": "CartonPalette not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
