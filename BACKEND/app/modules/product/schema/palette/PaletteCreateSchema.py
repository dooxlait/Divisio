# BACKEND/app/modules/product/schemas/palette/PaletteCreateSchema.py

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import pre_load
from app.core.extensions import db
from app.modules.product.models.palette import Palette

class PaletteCreateSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Palette
        load_instance = True
        include_fk = True
        sqla_session = db.session

    @pre_load
    def clean_strings(self, data, **kwargs):
        """
        Nettoie les champs string avant validation :
        - strip() de toutes les valeurs string
        - 'type' en majuscule
        """
        cleaned_data = dict(data)

        for key, value in cleaned_data.items():
            if isinstance(value, str):
                cleaned_data[key] = value.strip()

        if "type" in cleaned_data and isinstance(cleaned_data["type"], str):
            cleaned_data["type"] = cleaned_data["type"].upper()

        return cleaned_data
