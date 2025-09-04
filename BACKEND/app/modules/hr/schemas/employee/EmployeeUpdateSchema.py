# BACKEND\app\modules\hr\schemas\employee\EmployeeUpdateSchema.py

from marshmallow import Schema, fields, validates, ValidationError, pre_load
from datetime import date

class EmployeeUpdateSchema(Schema):
    first_name = fields.Str(required=False)
    last_name = fields.Str(required=False)
    matricule = fields.Str(required=False)
    hire_date = fields.Date(required=False)
    termination_date = fields.Date(required=False)

    @pre_load
    def clean_strings(self, data, **kwargs):
        """
        Nettoie les chaînes avant validation:
        - strip
        - capitalise les noms
        """
        cleaned = dict(data)
        for key, value in cleaned.items():
            if isinstance(value, str):
                cleaned[key] = value.strip()
        if "first_name" in cleaned:
            cleaned["first_name"] = cleaned["first_name"].title()
        if "last_name" in cleaned:
            cleaned["last_name"] = cleaned["last_name"].title()
        return cleaned

    @validates("matricule")
    def validate_matricule(self, value):
        if len(value) > 10:
            raise ValidationError("Le matricule ne doit pas dépasser 10 caractères.")

    @validates("hire_date")
    def validate_hire_date(self, value):
        if value > date.today():
            raise ValidationError("La date d'embauche ne peut pas être dans le futur.")

    @validates("termination_date")
    def validate_termination_date(self, value):
        if value and value > date.today():
            raise ValidationError("La date de fin ne peut pas être dans le futur.")
