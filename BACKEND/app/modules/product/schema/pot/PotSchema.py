# BACKEND/app/modules/product/schemas/pot/PotSchema.py

from marshmallow import fields
from app.common.base.base_schema import BaseSchema
from app.modules.product.models.pot import Pot

class PotSchema(BaseSchema):
    # Liste des produits finis utilisant ce pot
    produits = fields.List(fields.Nested("ProduitEmballageSchema", only=("id", "produit_fini_id")))

    class Meta:
        model = Pot
        load_instance = True
