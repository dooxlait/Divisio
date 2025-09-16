# BACKEND/app/modules/product/schemas/carton_palette/CartonPaletteCreateSchema.py

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import pre_load
from app.core.extensions import db
from app.modules.product.models.carton_palette import CartonPalette

class CartonPaletteCreateSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CartonPalette
        load_instance = True
        include_fk = True
        sqla_session = db.session

    @pre_load
    def clean_strings(self, data, **kwargs):
        """
        Nettoie les champs string avant validation.
        """
        cleaned_data = dict(data)

        for key, value in cleaned_data.items():
            if isinstance(value, str):
                cleaned_data[key] = value.strip()

        return cleaned_data
