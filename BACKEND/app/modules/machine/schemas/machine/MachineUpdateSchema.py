# BACKEND\app\modules\machine\schemas\machine\MachineUpdateSchema.py

from marshmallow import Schema, fields, pre_load

class MachineUpdateSchema(Schema):
    name = fields.Str(required=False)
    type = fields.Str(required=False)
    model = fields.Str(required=False)
    serial_number = fields.Str(required=False)
    manufacturer = fields.Str(required=False)
    
    parent_machine_id = fields.Str(required=False)
    site_id = fields.Str(required=False)
    division_id = fields.Str(required=False)

    @pre_load
    def clean_strings(self, data, **kwargs):
        cleaned = dict(data)
        for key, value in cleaned.items():
            if isinstance(value, str):
                cleaned[key] = value.strip()
        if "type" in cleaned:
            cleaned["type"] = cleaned["type"].upper()
        if "name" in cleaned:
            cleaned["name"] = cleaned["name"].title()
        return cleaned
