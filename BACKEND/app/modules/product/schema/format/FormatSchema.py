# BACKEND/app/modules/product/schemas/format/FormatSchema.py

from marshmallow import fields
from app.common.base.base_schema import BaseSchema
from app.modules.product.models.format import Format

class FormatSchema(BaseSchema):
    # Liste des produits finis utilisant ce format
    produits = fields.List(fields.Nested("ProduitFiniSchema", only=("id", "nom", "type_produit_id")))

    class Meta:
        model = Format
        load_instance = True
