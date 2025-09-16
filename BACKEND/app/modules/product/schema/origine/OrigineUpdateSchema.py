# BACKEND/app/modules/product/schemas/origine/OrigineUpdateSchema.py

from marshmallow import Schema, fields, pre_load

class OrigineUpdateSchema(Schema):
    nom = fields.Str(required=False)
    type_lait = fields.Str(required=False)  # ex: "vache", "brebis", "soja", etc.

    @pre_load
    def clean_strings(self, data, **kwargs):
        """
        Nettoie les champs string avant validation :
        - strip() de toutes les valeurs string
        - 'nom' en title case
        - 'type_lait' en majuscule
        """
        cleaned_data = dict(data)

        for key, value in cleaned_data.items():
            if isinstance(value, str):
                cleaned_data[key] = value.strip()

        if "nom" in cleaned_data and isinstance(cleaned_data["nom"], str):
            cleaned_data["nom"] = cleaned_data["nom"].title()

        if "type_lait" in cleaned_data and isinstance(cleaned_data["type_lait"], str):
            cleaned_data["type_lait"] = cleaned_data["type_lait"].upper()

        return cleaned_data
