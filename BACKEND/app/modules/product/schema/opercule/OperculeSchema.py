# BACKEND/app/modules/product/schemas/opercule/OperculeSchema.py

from marshmallow import fields
from app.common.base.base_schema import BaseSchema
from app.modules.product.models.opercule import Opercule

class OperculeSchema(BaseSchema):
    # Liste des produits utilisant cet opercule
    produits = fields.List(fields.Nested("ProduitEmballageSchema", only=("id", "produit_fini_id")))

    class Meta:
        model = Opercule
        load_instance = True
