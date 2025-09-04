# BACKEND\app\modules\machine\schemas\machine\MachineSchema.py

from marshmallow import fields

from app.common.base.base_schema import BaseSchema
from app.modules.machine.models.machine import Machine
from app.modules.factory.schemas.division.DivisionSchema import DivisionSchema


class MachineSchema(BaseSchema):
    # Sous-machines
    children = fields.List(fields.Nested("MachineSchema", only=("id", "name")))

    # Relation Division
    division = fields.Nested(DivisionSchema, only=("id", "name", "type"))

    class Meta:
        model = Machine
        load_instance = True
        # ❌ On n'inclut pas les FK pour éviter division_id et site_id
        include_fk = False