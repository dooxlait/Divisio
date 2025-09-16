# BACKEND/app/modules/product/schemas/carton/CartonSchema.py

from marshmallow import fields
from app.common.base.base_schema import BaseSchema
from app.modules.product.models.carton import Carton

class CartonSchema(BaseSchema):
    # Liste des produits associés via ProduitCarton
    produits = fields.List(fields.Nested("ProduitCartonSchema", only=("id", "produit_fini_id")))

    class Meta:
        model = Carton
        load_instance = True

# Schema pour création d'un carton
class CartonCreateSchema(BaseSchema):
    # Définis ici les champs nécessaires à la création
    nom = fields.Str(required=True)
    # autres champs si nécessaire

# Schema pour mise à jour d'un carton
class CartonUpdateSchema(BaseSchema):
    nom = fields.Str()
    # autres champs si nécessaire
