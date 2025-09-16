# BACKEND/app/modules/product/schemas/origine/OrigineSchema.py

from marshmallow import fields
from app.common.base.base_schema import BaseSchema
from app.modules.product.models.origine import Origine

class OrigineSchema(BaseSchema):
    # Liste des produits finis utilisant cette origine
    produits = fields.List(fields.Nested("ProduitFiniSchema", only=("id", "nom", "type_produit_id")))

    class Meta:
        model = Origine
        load_instance = True
