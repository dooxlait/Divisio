# BACKEND\app\modules\factory\schemas\division\DivisionUpdateSchema.py

from marshmallow import validates_schema, ValidationError, pre_load
from marshmallow import Schema, fields

class DivisionUpdateSchema(Schema):
    name = fields.Str(required=False)
    type = fields.Str(required=False)
    parent_id = fields.Str(required=False)
    site_id = fields.Str(required=False)

    @pre_load
    def clean_strings(self, data, **kwargs):
        """
        Nettoie et formate les champs string avant validation.
        - Strip de tous les champs string
        - 'type' en majuscule
        - 'name' en title case
        """
        cleaned_data = dict(data)  # Copier pour éviter modification directe

        # Strip et nettoyage pour toutes les valeurs string
        for key, value in cleaned_data.items():
            if isinstance(value, str):
                cleaned_data[key] = value.strip()


        # Champs spécifiques en majuscule
        if "type" in cleaned_data and isinstance(cleaned_data["type"], str):
            cleaned_data["type"] = cleaned_data["type"].upper()

        # 'name' en title case
        if "name" in cleaned_data and isinstance(cleaned_data["name"], str):
            cleaned_data["name"] = cleaned_data["name"].title()

        return cleaned_data
