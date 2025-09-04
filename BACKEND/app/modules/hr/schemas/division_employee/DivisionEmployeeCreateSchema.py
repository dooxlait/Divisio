# BACKEND/app/modules/hr/schemas/division_employee/DivisionEmployeeCreateSchema.py

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import pre_load, validates_schema, ValidationError, fields
from datetime import datetime
from app.modules.hr.models.division_employee import DivisionEmployee
from app.core.extensions import db

class DivisionEmployeeCreateSchema(SQLAlchemyAutoSchema):
    # Déclarer explicitement pour que Marshmallow sache que c'est une date
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=False, allow_none=True)

    class Meta:
        model = DivisionEmployee
        include_fk = True
        load_instance = True
        sqla_session = db.session

    @pre_load
    def clean_strings(self, data, **kwargs):
        """
        Nettoie et formate les champs string avant validation.
        - Strip de tous les champs string
        - 'type' en majuscule
        - 'name' en title case
        """
        cleaned_data = dict(data)  # Copier pour éviter modification directe

        # Strip et nettoyage pour toutes les valeurs string
        for key, value in cleaned_data.items():
            if isinstance(value, str):
                cleaned_data[key] = value.strip()

        # Champs spécifiques en majuscule
        if "role" in cleaned_data and isinstance(cleaned_data["role"], str):
            cleaned_data["role"] = cleaned_data["role"].upper()

        return cleaned_data

