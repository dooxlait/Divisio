# BACKEND/app/modules/product/schemas/variante/VarianteSchema.py

from marshmallow import fields
from app.common.base.base_schema import BaseSchema
from app.modules.product.models.variante import Variante

class VarianteSchema(BaseSchema):
    # Liste des produits finis de cette variante
    produits_finis = fields.List(fields.Nested("ProduitFiniSchema", only=("id", "nom", "type_produit_id", "origine_id")))

    class Meta:
        model = Variante
        load_instance = True
