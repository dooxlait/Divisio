# BACKEND/app/modules/product/schemas/produit_fini/ProduitFiniCreateSchema.py

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import pre_load
from app.core.extensions import db
from BACKEND.app.modules.product.models.produit_fini import ProduitFini

class ProduitFiniCreateSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ProduitFini
        load_instance = True
        include_fk = True
        sqla_session = db.session

    @pre_load
    def clean_strings(self, data, **kwargs):
        """
        Nettoie les champs string avant validation :
        - strip() de toutes les valeurs string
        - 'nom' en title case
        """
        cleaned_data = dict(data)

        for key, value in cleaned_data.items():
            if isinstance(value, str):
                cleaned_data[key] = value.strip()

        if "nom" in cleaned_data and isinstance(cleaned_data["nom"], str):
            cleaned_data["nom"] = cleaned_data["nom"].title()

        return cleaned_data
