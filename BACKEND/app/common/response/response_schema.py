# BACKEND\app\common\response\response_schema.py

from marshmallow import Schema, fields

class APIResponseSchema(Schema):
    status = fields.Str(required=True)  # "success" ou "error"
    payload = fields.Raw(allow_none=True)  # n'importe quelle donnée (liste, dict, etc.)
    message = fields.Str(allow_none=True)