# BACKEND/app/modules/product/schemas/carton_palette/CartonPaletteSchema.py

from marshmallow import fields
from app.common.base.base_schema import BaseSchema
from app.modules.product.models.carton_palette import CartonPalette

class CartonPaletteSchema(BaseSchema):
    carton = fields.Nested("CartonSchema", only=("id", "nom", "capacite", "type"))
    palette = fields.Nested("PaletteSchema", only=("id", "type", "cartons_par_couche", "nb_couches"))

    class Meta:
        model = CartonPalette
        load_instance = True
