# BACKEND/app/modules/product/schemas/carton/CartonCreateSchema.py

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import pre_load
from app.core.extensions import db
from app.modules.product.models.carton import Carton

class CartonCreateSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Carton
        load_instance = True
        include_fk = True
        sqla_session = db.session

    @pre_load
    def clean_strings(self, data, **kwargs):
        """
        Nettoie les champs string avant validation :
        - strip() de toutes les valeurs string
        - 'type' en majuscule
        - 'nom' en title case
        """
        cleaned_data = dict(data)

        for key, value in cleaned_data.items():
            if isinstance(value, str):
                cleaned_data[key] = value.strip()

        if "type" in cleaned_data and isinstance(cleaned_data["type"], str):
            cleaned_data["type"] = cleaned_data["type"].upper()

        if "nom" in cleaned_data and isinstance(cleaned_data["nom"], str):
            cleaned_data["nom"] = cleaned_data["nom"].title()

        return cleaned_data
