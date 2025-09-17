# BACKEND/app/modules/product/routes/palette_routes.py

from flask import Blueprint, request, jsonify
from app.modules.product.services.palette_service import PaletteService
from app.modules.product.schema.palette.PaletteSchema import PaletteSchema
from app.modules.product.schema.palette.PaletteCreateSchema import PaletteCreateSchema
from app.modules.product.schema.palette.PaletteUpdateSchema import PaletteUpdateSchema

palette_bp = Blueprint("palette_bp", __name__, url_prefix="/palettes")
service = PaletteService()

# GET /palettes → liste toutes les palettes
@palette_bp.route("/", methods=["GET"])
def get_all_palettes():
    palettes = service.get_all()
    schema = PaletteSchema(many=True)
    return jsonify(schema.dump(palettes)), 200

# GET /palettes/<id> → récupère une palette par ID
@palette_bp.route("/<string:palette_id>", methods=["GET"])
def get_palette(palette_id):
    palette = service.get_by_id(palette_id)
    if not palette:
        return jsonify({"message": "Palette not found"}), 404
    schema = PaletteSchema()
    return jsonify(schema.dump(palette)), 200

# POST /palettes → crée une nouvelle palette
@palette_bp.route("/", methods=["POST"])
def create_palette():
    data = request.get_json()
    schema = PaletteCreateSchema()
    validated_data = schema.load(data)
    palette = service.create(validated_data)
    return jsonify(PaletteSchema().dump(palette)), 201

# PUT /palettes/<id> → met à jour une palette
@palette_bp.route("/<string:palette_id>", methods=["PUT"])
def update_palette(palette_id):
    data = request.get_json()
    schema = PaletteUpdateSchema()
    validated_data = schema.load(data, partial=True)
    palette = service.update(palette_id, validated_data)
    if not palette:
        return jsonify({"message": "Palette not found"}), 404
    return jsonify(PaletteSchema().dump(palette)), 200

# DELETE /palettes/<id> → supprime une palette
@palette_bp.route("/<string:palette_id>", methods=["DELETE"])
def delete_palette(palette_id):
    success = service.delete(palette_id)
    if not success:
        return jsonify({"message": "Palette not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
