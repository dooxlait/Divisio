# BACKEND\app\modules\hr\schemas\employee\EmployeeSchema.py

from app.common.base.base_schema import BaseSchema
from app.modules.hr.models.employee import Employee

class EmployeeSchema(BaseSchema):
    class Meta:
        model = Employee