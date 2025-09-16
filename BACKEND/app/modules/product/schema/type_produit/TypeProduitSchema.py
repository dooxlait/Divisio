# BACKEND/app/modules/product/schemas/type_produit/TypeProduitSchema.py

from marshmallow import fields
from app.common.base.base_schema import BaseSchema
from app.modules.product.models.type_produit import TypeProduit

class TypeProduitSchema(BaseSchema):
    # Liste des produits finis de ce type
    produits_finis = fields.List(fields.Nested("ProduitFiniSchema", only=("id", "nom", "variante_id", "origine_id")))

    class Meta:
        model = TypeProduit
        load_instance = True
