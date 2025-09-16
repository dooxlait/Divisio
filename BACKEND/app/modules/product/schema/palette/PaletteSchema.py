# BACKEND/app/modules/product/schemas/palette/PaletteSchema.py

from marshmallow import fields
from app.common.base.base_schema import BaseSchema
from app.modules.product.models.palette import Palette

class PaletteSchema(BaseSchema):
    # Liste des cartons associés à la palette via CartonPalette
    cartons = fields.List(fields.Nested("CartonPaletteSchema", only=("id", "carton_id", "quantite")))

    class Meta:
        model = Palette
        load_instance = True
