# BACKEND/app/modules/product/schemas/produit_emballage/ProduitEmballageUpdateSchema.py

from marshmallow import Schema, fields, pre_load

class ProduitEmballageUpdateSchema(Schema):
    pot_id = fields.Str(required=False)
    coiffe_id = fields.Str(required=False)
    opercule_id = fields.Str(required=False)
    format_id = fields.Str(required=False)

    @pre_load
    def clean_strings(self, data, **kwargs):
        """
        Nettoie les champs string avant validation
        """
        cleaned_data = dict(data)

        for key, value in cleaned_data.items():
            if isinstance(value, str):
                cleaned_data[key] = value.strip()

        return cleaned_data
