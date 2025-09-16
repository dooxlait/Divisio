# BACKEND/app/modules/product/schemas/coiffe/CoiffeSchema.py

from marshmallow import fields
from app.common.base.base_schema import BaseSchema
from app.modules.product.models.coiffe import Coiffe

class CoiffeSchema(BaseSchema):
    # Liste des produits utilisant cette coiffe
    produits = fields.List(fields.Nested("ProduitEmballageSchema", only=("id", "produit_fini_id")))

    class Meta:
        model = Coiffe
        load_instance = True
