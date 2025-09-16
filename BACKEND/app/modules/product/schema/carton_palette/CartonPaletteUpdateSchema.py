# BACKEND/app/modules/product/schemas/carton_palette/CartonPaletteUpdateSchema.py

from marshmallow import Schema, fields, pre_load

class CartonPaletteUpdateSchema(Schema):
    carton_id = fields.Str(required=False)
    palette_id = fields.Str(required=False)
    quantite = fields.Int(required=False)

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
