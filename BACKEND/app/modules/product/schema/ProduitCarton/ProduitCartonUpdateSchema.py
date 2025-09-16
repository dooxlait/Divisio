# BACKEND/app/modules/product/schema/ProduitCarton/ProduitCartonUpdateSchema.py

from marshmallow import Schema, fields, pre_load

class ProduitCartonUpdateSchema(Schema):
    produit_fini_id = fields.Str(required=False)
    carton_id = fields.Str(required=False)
    quantite = fields.Int(required=False)

    @pre_load
    def clean_strings(self, data, **kwargs):
        cleaned_data = dict(data)
        for key, value in cleaned_data.items():
            if isinstance(value, str):
                cleaned_data[key] = value.strip()
        return cleaned_data
