# BACKEND/app/modules/product/schemas/produit_emballage/ProduitEmballageSchema.py

from marshmallow import fields
from app.common.base.base_schema import BaseSchema
from app.modules.product.models.produit_emballage import ProduitEmballage

class ProduitEmballageSchema(BaseSchema):
    # Relations vers les composants d'emballage
    pot = fields.Nested("PotSchema", only=("id", "nom", "matiere", "volume_ml"))
    coiffe = fields.Nested("CoiffeSchema", only=("id", "nom", "matiere", "design"))
    opercule = fields.Nested("OperculeSchema", only=("id", "nom", "matiere", "design"))
    format = fields.Nested("FormatSchema", only=("id", "nom", "poids_g"))

    class Meta:
        model = ProduitEmballage
        load_instance = True
