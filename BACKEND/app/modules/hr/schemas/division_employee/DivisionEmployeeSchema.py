# BACKEND/app/modules/hr/schemas/division_employee/DivisionEmployeeSchema.py

# BACKEND/app/modules/hr/schemas/division_employee/DivisionEmployeeSchema.py

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from app.modules.hr.models.division_employee import DivisionEmployee
from app.modules.factory.schemas.division.DivisionSchema import DivisionSchema
from app.modules.hr.schemas.employee.EmployeeSchema import EmployeeSchema
from app.core.extensions import db

class DivisionEmployeeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = DivisionEmployee
        load_instance = True
        sqla_session = db.session
        include_fk = True

    start_date = fields.Date()
    end_date = fields.Date(allow_none=True)

    # Nested pour les relations
    division = fields.Nested(DivisionSchema, only=("id", "name", "type"))
    employee = fields.Nested(EmployeeSchema, only=("id", "first_name", "last_name", "matricule"))


    # Champs enrichis (via relations)
    # division_id = fields.UUID(attribute="division.id")
    # division_name = fields.String(attribute="division.name")
    # division_type = fields.String(attribute="division.type")
    # employee_name = fields.String(attribute="employee.name")