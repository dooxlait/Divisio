# BACKEND/app/modules/hr/schemas/division_employee/DivisionEmployeeUpdateSchema.py

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, pre_load, validates_schema, ValidationError
from app.modules.hr.models.division_employee import DivisionEmployee
from app.core.extensions import db
from datetime import datetime

class DivisionEmployeeUpdateSchema(SQLAlchemyAutoSchema):
    # Déclarer explicitement les champs date pour Marshmallow
    start_date = fields.Date(required=False)
    end_date = fields.Date(required=False, allow_none=True)
    role = fields.Str(required=False)

    class Meta:
        model = DivisionEmployee
        load_instance = False
        sqla_session = db.session
        include_fk = True

    @pre_load
    def clean_input(self, data, **kwargs):
        """
        Nettoyage des chaînes et conversion des dates si nécessaire.
        """
        cleaned_data = dict(data)

        # Strip pour tous les champs string
        for key, value in cleaned_data.items():
            if isinstance(value, str):
                cleaned_data[key] = value.strip()

        # Majuscule pour le rôle
        if "role" in cleaned_data and isinstance(cleaned_data["role"], str):
            cleaned_data["role"] = cleaned_data["role"].upper()

        # Conversion des dates string -> datetime.date
        for field in ["start_date", "end_date"]:
            if field in cleaned_data and isinstance(cleaned_data[field], str):
                try:
                    cleaned_data[field] = datetime.strptime(cleaned_data[field], "%Y-%m-%d").date()
                except ValueError:
                    raise ValidationError({field: ["Le format doit être YYYY-MM-DD."]})

        return cleaned_data

    @validates_schema
    def validate_dates(self, data, **kwargs):
        """
        Vérifie que end_date >= start_date si end_date fourni.
        """
        start_date = data.get("start_date")
        end_date = data.get("end_date")

        if start_date and end_date and end_date < start_date:
            raise ValidationError({"end_date": ["La date de fin ne peut pas être antérieure à la date de début."]})
