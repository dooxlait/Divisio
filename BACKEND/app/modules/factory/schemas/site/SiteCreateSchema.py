# BACKEND\app\modules\factory\schemas\factory\FactoryCreateSchema.py

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import validates_schema, ValidationError, pre_load

from app.core.extensions import db
from app.modules.factory.models.site import Site


class SiteCreateSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Site
        load_instance = True
        include_fk = True          # corrigé : 'includ_fk' → 'include_fk'
        sqla_session = db.session 

    @pre_load
    def clean_strings(self, data, **kwargs):
        # Copier le dict pour éviter modification directe
        cleaned_data = dict(data)

        # Strip et nettoyage pour toutes les valeurs string
        for key, value in cleaned_data.items():
            if isinstance(value, str):
                cleaned_data[key] = value.strip()

        # Champs spécifiques en majuscule
        for field in ["name", "city", "country"]:
            if field in cleaned_data and isinstance(cleaned_data[field], str):
                cleaned_data[field] = cleaned_data[field].upper()

        # Adresse en title case
        if "address" in cleaned_data and isinstance(cleaned_data["address"], str):
            cleaned_data["address"] = cleaned_data["address"].title()

        return cleaned_data

    @validates_schema
    def validate_names(self, data, **kwargs):
        if not kwargs.get("partial", False):
            required_fields = ["name", "city", "country", "address"]
            missing = [f for f in required_fields if not data.get(f)]
            if missing:
                raise ValidationError(f"Les champs obligatoires sont manquants : {', '.join(missing)}")
