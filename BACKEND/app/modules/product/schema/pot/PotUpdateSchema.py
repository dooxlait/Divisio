# BACKEND/app/modules/product/schemas/pot/PotUpdateSchema.py

from marshmallow import Schema, fields, pre_load

class PotUpdateSchema(Schema):
    nom = fields.Str(required=False)
    matiere = fields.Str(required=False)
    volume_ml = fields.Int(required=False)

    @pre_load
    def clean_strings(self, data, **kwargs):
        """
        Nettoie les champs string avant validation :
        - strip() de toutes les valeurs string
        - 'nom' en title case
        - 'matiere' en majuscule
        """
        cleaned_data = dict(data)

        for key, value in cleaned_data.items():
            if isinstance(value, str):
                cleaned_data[key] = value.strip()

        if "nom" in cleaned_data and isinstance(cleaned_data["nom"], str):
            cleaned_data["nom"] = cleaned_data["nom"].title()

        if "matiere" in cleaned_data and isinstance(cleaned_data["matiere"], str):
            cleaned_data["matiere"] = cleaned_data["matiere"].upper()

        return cleaned_data
