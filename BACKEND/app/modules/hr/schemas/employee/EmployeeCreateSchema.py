# BACKEND\app\modules\hr\schemas\employee\EmployeeCreateSchema.py
from datetime import date

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import validates_schema, ValidationError, pre_load, validates

from app.core.extensions import db
from app.modules.hr.models.employee import Employee

class EmployeeCreateSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        include_fk = True
        load_instance = True
        sqla_session = db.session

    @pre_load
    def clean_input(self, data, **kwargs):
        cleaned_data = dict(data)

        # Strip et nettoyage
        for key, value in cleaned_data.items():
            if isinstance(value, str):
                cleaned_data[key] = value.strip()

        # Capitalisation / majuscule
        if "first_name" in cleaned_data and isinstance(cleaned_data["first_name"], str):
            cleaned_data["first_name"] = cleaned_data["first_name"].title()
        if "last_name" in cleaned_data and isinstance(cleaned_data["last_name"], str):
            cleaned_data["last_name"] = cleaned_data["last_name"].upper()
        
        # Matricule : si fourni, on complète à 10 caractères
        if "matricule" in cleaned_data and isinstance(cleaned_data["matricule"], str):
            cleaned_data["matricule"] = cleaned_data["matricule"].zfill(10)
        # Si matricule non fourni, on le génère automatiquement
        elif "matricule" not in cleaned_data or not cleaned_data["matricule"]:
            last_employee = Employee.query.order_by(Employee.matricule.desc()).first()
            if last_employee and last_employee.matricule.isdigit():
                new_number = int(last_employee.matricule) + 1
            else:
                new_number = 1
            cleaned_data["matricule"] = str(new_number).zfill(10)

        return cleaned_data

    @validates("matricule")
    def validate_unique_matricule(self, value):
        if Employee.query.filter_by(matricule=value).first():
            raise ValidationError(f"Le matricule '{value}' est déjà utilisé.")
        
    @validates_schema
    def validate_dates(self, data, **kwargs):
        hire_date = data.get("hire_date")
        termination_date = data.get("termination_date")

        if hire_date and termination_date and termination_date < hire_date:
            raise ValidationError("La date de fin ne peut pas être antérieure à la date d'embauche.", field_name="termination_date")
