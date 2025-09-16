# BACKEND/app/modules/product/schema/ProduitCarton/ProduitCartonSchema.py

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import validates_schema, ValidationError, pre_load
from app.core.extensions import db
from app.modules.product.models.produit_carton import ProduitCarton


class ProduitCartonSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ProduitCarton
        load_instance = True
        include_fk = True
        sqla_session = db.session

    @pre_load
    def clean_strings(self, data, **kwargs):
        """
        Nettoie les champs string avant validation.
        - Strip de tous les champs string
        """
        cleaned_data = dict(data)
        for key, value in cleaned_data.items():
            if isinstance(value, str):
                cleaned_data[key] = value.strip()
        return cleaned_data
