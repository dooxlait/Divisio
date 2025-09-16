# BACKEND/app/modules/product/schema/ProduitCarton/ProduitCartonCreateSchema.py

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import pre_load
from app.core.extensions import db
from modules.product.models.produit_carton import ProduitCarton

class ProduitCartonCreateSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ProduitCarton
        load_instance = True
        include_fk = True
        sqla_session = db.session

    @pre_load
    def clean_strings(self, data, **kwargs):
        cleaned_data = dict(data)
        for key, value in cleaned_data.items():
            if isinstance(value, str):
                cleaned_data[key] = value.strip()
        return cleaned_data
