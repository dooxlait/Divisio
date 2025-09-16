# BACKEND/app/modules/product/schemas/produit_fini/ProduitFiniSchema.py

from marshmallow import fields
from app.common.base.base_schema import BaseSchema
from BACKEND.app.modules.product.models.produit_fini import ProduitFini

class ProduitFiniSchema(BaseSchema):
    # Relations
    type_produit = fields.Nested("TypeProduitSchema", only=("id", "nom"))
    variante = fields.Nested("VarianteSchema", only=("id", "nom"))
    origine = fields.Nested("OrigineSchema", only=("id", "nom", "type_lait"))

    emballages = fields.List(fields.Nested("ProduitEmballageSchema", 
        only=("id", "pot", "coiffe", "opercule", "format")))

    class Meta:
        model = ProduitFini
        load_instance = True
