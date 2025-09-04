# BACKEND\app\modules\factory\schemas\division\DivisionSchema.py

from marshmallow import fields

from app.common.base.base_schema import BaseSchema
from app.modules.factory.models.division import Division


class DivisionSchema(BaseSchema):
    subdivisions = fields.List(fields.Nested("DivisionSchema", only=("id", "name")))

    class Meta:
        model = Division
        load_instance = True