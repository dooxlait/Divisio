# BACKEND/app/modules/product/schemas/palette/PaletteUpdateSchema.py

from marshmallow import Schema, fields, pre_load

class PaletteUpdateSchema(Schema):
    type = fields.Str(required=False)
    nb_couches = fields.Int(required=False)
    cartons_par_couche = fields.Int(required=False)

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
