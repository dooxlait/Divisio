# BACKEND\app\modules\machine\schemas\machine_document\MachineDocumentCreateSchema.py

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import validates_schema, ValidationError, pre_load

from app.core.extensions import db
from app.modules.machine.models.machine_document import MachineDocument

class MachineDocumentCreateSchema():
    class Meta:
        model = MachineDocument
        load_instance = True
        include_fk = True
        sqla_session = db.session  # Correctement placé au niveau de Meta